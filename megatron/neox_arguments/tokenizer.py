from dataclasses import dataclass

@dataclass
class NeoXArgsTokenizer:

    tokenizer_type: str = "GPT2BPETokenizer"
    """"""

    padded_vocab_size: int = None
    """"""