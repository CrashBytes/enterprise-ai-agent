"""Configuration management with environment variable loading."""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field, validator

# Load environment variables
load_dotenv()

class OpenAIConfig(BaseModel):
    """OpenAI API configuration."""
    api_key: str = Field(..., env='OPENAI_API_KEY')
    model: str = Field(default='gpt-4-turbo-preview', env='OPENAI_MODEL')
    temperature: float = Field(default=0.0, env='OPENAI_TEMPERATURE')
    max_tokens: int = Field(default=4096, env='MAX_TOKENS')
    
    @validator('api_key')
    def validate_api_key(cls, v):
        if not v or v == 'your_openai_api_key_here':
            raise ValueError('Valid OpenAI API key required')
        return v

class AgentConfig(BaseModel):
    """Agent behavior configuration."""
    max_iterations: int = Field(default=10, env='AGENT_MAX_ITERATIONS')
    max_execution_time: int = Field(default=300, env='AGENT_MAX_EXECUTION_TIME')
    verbose: bool = Field(default=True, env='AGENT_VERBOSE')
    
    @validator('max_iterations')
    def validate_iterations(cls, v):
        if v < 1 or v > 50:
            raise ValueError('Max iterations must be between 1 and 50')
        return v

class MemoryConfig(BaseModel):
    """Memory and persistence configuration."""
    memory_type: str = Field(default='chromadb', env='MEMORY_TYPE')
    collection_name: str = Field(default='agent_memory', env='MEMORY_COLLECTION_NAME')
    persist_directory: Path = Field(default=Path('./data/memory'), env='MEMORY_PERSIST_DIRECTORY')

class CostConfig(BaseModel):
    """Cost tracking and budget configuration."""
    max_cost_per_request: float = Field(default=1.00, env='MAX_COST_PER_REQUEST')
    enable_cost_tracking: bool = Field(default=True, env='ENABLE_COST_TRACKING')

class Config(BaseModel):
    """Master configuration object."""
    openai: OpenAIConfig = OpenAIConfig(
        api_key=os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here'),
        model=os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview'),
        temperature=float(os.getenv('OPENAI_TEMPERATURE', '0.0')),
        max_tokens=int(os.getenv('MAX_TOKENS', '4096'))
    )
    agent: AgentConfig = AgentConfig(
        max_iterations=int(os.getenv('AGENT_MAX_ITERATIONS', '10')),
        max_execution_time=int(os.getenv('AGENT_MAX_EXECUTION_TIME', '300')),
        verbose=os.getenv('AGENT_VERBOSE', 'true').lower() == 'true'
    )
    memory: MemoryConfig = MemoryConfig(
        memory_type=os.getenv('MEMORY_TYPE', 'chromadb'),
        collection_name=os.getenv('MEMORY_COLLECTION_NAME', 'agent_memory'),
        persist_directory=Path(os.getenv('MEMORY_PERSIST_DIRECTORY', './data/memory'))
    )
    cost: CostConfig = CostConfig(
        max_cost_per_request=float(os.getenv('MAX_COST_PER_REQUEST', '1.00')),
        enable_cost_tracking=os.getenv('ENABLE_COST_TRACKING', 'true').lower() == 'true'
    )
    
    @classmethod
    def load(cls) -> 'Config':
        """Load configuration from environment."""
        return cls()

# Global configuration instance
config = Config.load()
