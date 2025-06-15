from util.llm_factory import LLMFactory
import os

from util.system_prompt import prompt_generate_summary
def generate_summary(text):
    """
    Generates a summary of the given text using the LLM.
    """
    response = LLMFactory.invoke(
        system_prompt=prompt_generate_summary,
        human_message=text,
        temperature=0.7,
        local_llm=False,
    )
    summary = response.content.strip()
    return summary



if __name__ == "__main__":
    Question = "Canyou tell me about shadowwriting, a method, probably, discord used to transfer its humungus database"
    summary = generate_summary(Question)
    print("\nGenerated Summary:")
    print(summary)
