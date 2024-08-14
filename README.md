# 2024_AI_playground
trying some AI model
<br/><br/>

## OpenAI Whisper 
1. speech to text model
2. https://github.com/openai/whisper
3. using `pip install -U openai-whisper` to install; the GitHub version could be newer.
4. "whisper_old.py": First attempt. Convert the output to str by using my own method.
5. "whisper_utils.py": Found that Whisper has built-in methods. Try mandarin audio.
<br/><br/>

### TODO
1. add the `ffmpeg` function to convert video to audio.
### Known issues
1. If the audio file contains multiple languages, it may miss parts of the text.
    - It might be related to the length of the trim.



## Meta-Llama-3.1-8B-Instruct
1. 8B, instruction-tuned version of Llama 3.1
2. https://ai.meta.com/blog/meta-llama-3-1/
3. https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct

### TODO
1. create a py file to run Llama locally
2. build an API with FastAPI


## My system
1. windows 11 23H2
2. 12th Gen Intel Core i3-12100F   3.30 GHz
3. NVIDIA GeForce RTX 3070 8GB
4. CUDA Version: 12.5