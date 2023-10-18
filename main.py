import ffmpeg
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.camera import Camera

class MyApp(App):
    def build(self):
        self.label = Label(text="Initial Label Text")
        camera = Camera()
        try:
            # Create an ffmpeg.input() object for the camera feed.
            camera_input = ffmpeg.input(camera.texture)
            print(camera_input)

            # Create an ffmpeg.output() object for the network server.
            network_output = ffmpeg.output(camera_input, format='flv', rtmp='rtmp://192.168.0.104:1935/live/stream')

            # Specify the video and audio codecs and other encoding parameters.
            network_output.video.codec = 'libx264'
            network_output.video.bitrate = 2000000
            network_output.audio.codec = 'aac'
            network_output.audio.bitrate = 128000

            # Pipe the output of the ffmpeg.input() object to the input of the ffmpeg.output() object.
            ffmpeg.run(camera_input, network_output)
            self.label.text = 'Stream is working!'
        except Exception as e:
            self.label.text = 'Error: {}'.format(e)
if __name__ == '__main__':
    MyApp().run()