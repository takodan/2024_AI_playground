import whisper
from whisper.utils import get_writer
import time

input_path = "sample/約旦奇遇_chinese.m4a"
output_path = "sample/"
output_name = "約旦奇遇_chinese"
# txt, vtt, srt, tsv, json, all
output_format = "srt"
outline = "約旦奇遇"

# tiny, tiny.en, base, base.en, small, small.en, medium, medium.en
whisper_model = "medium"

# Load the model
model = whisper.load_model(whisper_model) # device="cuda" if available

time_start = time.time()
print("\ntranscribe START\n")
# Transcribe the audio
result = model.transcribe(
    audio = input_path,
    # verbose: Optional[bool] = None,
    # temperature: Union[float, Tuple[float, ...]] = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
    # compression_ratio_threshold: Optional[float] = 2.4,
    # logprob_threshold: Optional[float] = -1.0,
    # no_speech_threshold: Optional[float] = 0.6,
    # condition_on_previous_text: bool = True,
    # initial_prompt: Optional[str] = None,
    initial_prompt = outline,
    # word_timestamps: bool = False,
    word_timestamps = True,
    # prepend_punctuations: str = "\"'“¿([{-",
    # append_punctuations: str = "\"'.。,，!！?？:：”)]}、",
    # **decode_options,
    )

time_end = time.time()
print(f"\ntranscribe END, cost {round(time_end-time_start, 3)} sec\n")

writer = get_writer(output_format, output_path)
writer(result, output_name)
