import pytest
from unittest.mock import Mock, patch
from langchain_core.language_models.fake import FakeListLLM
from langchain_core.messages import AIMessage
from langgraph_agent.agent import create_graph, process_message, State

def test_create_graph_structure():
    """Test czy graf się kompiluje poprawnie"""
    graph = create_graph()
    assert graph is not None

def test_chatbot_basic_structure():
    """Test czy graf ma poprawną strukturę"""
    graph = create_graph()
    # Test że graf ma nodes
    assert hasattr(graph, 'nodes')

@patch('agent.init_chat_model')
def test_process_message_with_fake_llm(mock_init_chat_model):
    """Test z Fake LLM - nie wywołuje prawdziwego API"""
    # Użyj FakeListLLM zamiast Mocka
    fake_llm = FakeListLLM(responses=["This is a test response"])
    mock_init_chat_model.return_value = fake_llm
    
    # Test
    response = process_message("Hello")
    assert response == "This is a test response"
    assert mock_init_chat_model.called

def test_graph_state_structure():
    """Test czy State ma poprawną strukturę"""
    from typing import get_type_hints
    hints = get_type_hints(State)
    assert 'messages' in hints
