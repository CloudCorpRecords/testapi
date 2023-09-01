from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
import os
import uuid

def merge_images_audio(image_folder, audio_folder, output_folder, video_size=(1080, 1920)):
    image_files = sorted([os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(('.jpg', '.png'))])
    audio_file = [os.path.join(audio_folder, file) for file in os.listdir(audio_folder) if file.endswith(('.mp3', '.wav'))][0]

    image_duration = 3.5  # Duration for each image in seconds
    video_duration = image_duration * len(image_files)

    def centered_image_clip(img_path, size):
        img_clip = ImageClip(img_path).resize(video_size)  # Resize image to video_size
        return img_clip.set_position("center").set_duration(image_duration)

    image_clips = [centered_image_clip(image, video_size) for image in image_files]
    final_video = concatenate_videoclips(image_clips)

    audio_clip = AudioFileClip(audio_file).subclip(0, video_duration)  # Trim or loop audio to match video duration
    final_video = final_video.set_audio(audio_clip)

    output_filename = os.path.join(output_folder, "output.mp4")
    if os.path.exists(output_filename):
        output_filename = f"{output_filename.split('.')[0]}_{str(uuid.uuid4())[:8]}.{output_filename.split('.')[1]}"

    final_video.write_videofile(output_filename, codec='libx264', fps=24)

if _name_ == "_main_":
    image_folder = r"C:\Users\cloud\Documents\jeff\image_folder"  # Path to the folder containing images
    audio_folder = r"C:\Users\cloud\Documents\jeff\audio_folder"  # Path to the folder containing the audio file (MP3 or WAV)
    output_folder = r"C:\Users\cloud\Documents\jeff\output_folder"  # Path to the folder where the output video will be saved

    merge_images_audio(image_folder, audio_folder, output_folder)
