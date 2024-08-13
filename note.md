## whisper
- https://github.com/openai/whisper
1. install **whisper** `pip install -U openai-whisper`
2. install **ffmpeg** on Windows using Chocolatey `choco install ffmpeg`
3. may need **rust** installed as well https://www.rust-lang.org/learn/get-started
4. srt file format https://github.com/openai/whisper/discussions/98


## debug (windows11)
1. check CUDA version `cmd`: `nvidia-smi`
2. install PyTorch with CUDA support `cmd`: `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`
3. pip install without catch `cmd`: `--no-cache-dir`
4. pip force reinstall `cmd`: `pip install --upgrade --force-reinstall`
5. **INFO OSError: [WinError 126] The specified module could not be found. Error loading** https://github.com/Acly/krita-ai-diffusion/issues/965
6. pip delete catch `cmd`: `pip cache purge`