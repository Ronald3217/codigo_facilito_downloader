"""
Video download model
"""

import time

from ..errors import DownloadError


class YoutubeDLLogger:
    """Custom yt-dlp logger"""

    def debug(self, msg):
        """Debug message"""

    def info(self, msg):
        """Info message"""

    def warning(self, msg):
        """Warning message"""

    def error(self, msg):
        """Error message"""
        raise DownloadError(f"Downloading video failed. {msg}")

    @staticmethod
    def wrapper_hook(file_name: str):
        """
        A static method that serves as a wrapper hook for a progress callback function.
        It takes a file name as a parameter and returns a callback
        function based on the progress of the download.
        The callback function prints messages based on the download status
        and sleeps for 0.1 seconds during downloading.
        Parameters:
        file_name (str): The name of the file being downloaded.
        Returns:
        callable: A callback function for monitoring the progress of the download.
        """

        def on_progress(d: dict):
            """Progress callback"""
            if d["status"] == "finished":
                print("Done downloading")
            elif d["status"] == "downloading":
                print(
                    f"\rDownloading... {file_name}. {d['_default_template']} ",
                    end="",
                    flush=True,
                )
                time.sleep(0.1)
            elif d["status"] == "error":
                print(f"Error during download: {d['error']}")

        return on_progress
