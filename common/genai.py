from enum import Enum
import os
import assemblyai as aai
import yt_dlp
from typing import Dict, Union
from pydantic import BaseModel
from common.model import Analysis, Clip
from common.prompts import BASE_PROMPT, TRANSCRIPT
from langchain_openai import ChatOpenAI
from langchain.chat_models.base import BaseChatModel
from langchain_core.runnables import RunnableSerializable, RunnableLambda
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv, find_dotenv
from loguru import logger


class Provider(str, Enum):
    OPENAI = "openai"

class LLM(str, Enum):
    GPT_4o = "gpt-4o"


class ModelGateway:
    provider_model_map: Dict[Provider, Dict[LLM, BaseModel]] = {
        Provider.OPENAI: {
            "supported_models": [LLM.GPT_4o],
            "langchain_adapter": ChatOpenAI
        }
    }
    @classmethod
    def get_adapter(
        cls,
        provider: Provider,
        model: LLM,
        **kwargs
    ) -> Union[BaseChatModel]:
        """
        Returns an initialized langchain adapter for the given provider and model where any passed kwargs are passed to the adapter such as temperature, top_p, etc.
        """
        return cls.provider_model_map[provider]["langchain_adapter"](model=model, **kwargs)


def init_transcript_analysis_chain(
    client_id: str = "Google"
) -> RunnableSerializable:
    
    parser = PydanticOutputParser(pydantic_object = Analysis)
    
    chain = (
        PromptTemplate(
            template = BASE_PROMPT,
            input_variables=["transcript"],
            partial_variables={
                "format_instructions": parser.get_format_instructions()
            }
        )
        | ModelGateway.get_adapter(provider=Provider.OPENAI, model=LLM.GPT_4o)
        | parser
    ).with_config({"run_name": f"Transcript Analysis - {client_id}"})
    return chain


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    chain = init_transcript_analysis_chain()
    print(chain.invoke(TRANSCRIPT))
