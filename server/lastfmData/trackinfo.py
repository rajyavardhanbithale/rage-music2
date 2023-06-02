import soundfile as sf

# Compress audio using Opus
def compress_audio(input_file, output_file, compression_level=192):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Export as Opus
    audio.export(output_file, format="opus", parameters=["-compression_level", str(compression_level)])


# Example usage
input_file = "Giveon - Heartbreak Anniversary (Audio) [nja_0BaQcNg].mp3"  # Replace with the path to your input audio file
output_file = "out.opus"  # Replace with the desired path for the output compressed file
compression_level = 5  # Adjust the compression level as needed (0-10, where 0 is lowest and 10 is highest)

compress_audio(input_file, output_file, compression_level)
