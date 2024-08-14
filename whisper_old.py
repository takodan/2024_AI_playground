import whisper
import datetime
import time

input_path: str = "sample/test_short.m4a"
output_path: str = "sample/test_short.srt"
outline: str = "Bae's Mom Thought that Bae Finally got a Boyfriend"

# tiny, tiny.en, base, base.en, small, small.en, medium, medium.en
whisper_model = "base"

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
print(f"\ntranscribe END, cost {time_end-time_start} sec\n")

# show 10 sample
for segment in result["segments"][:10]:
    print(f"{round(segment['start'], 2)} to {round(segment['end'], 2)}: \n {segment['text']}\n")

# save segments as srt file
segments = result['segments']
srt_lines = []
end_time_delay = 1.01
for i, segment in enumerate(segments):
    start = str(datetime.timedelta(seconds=round(segment['start'], 2)))
    if len(start) < 14:
        start = start + "," + "0"*(13-len(start))
    start_srt = start[:-3].replace(".", ",")

    end = str(datetime.timedelta(seconds=round(segment['end'], 2)*end_time_delay))
    if len(end) < 14:
        end = end + "," + "0"*(13-len(end))
    end_srt = end[:-3].replace(".", ",")
    text = segment['text'].strip()
    srt_lines.append(f"{i + 1}\n{start_srt} --> {end_srt}\n{text}\n")

with open(output_path, "w", encoding="utf-8") as srt_file:
    srt_file.writelines(srt_lines)