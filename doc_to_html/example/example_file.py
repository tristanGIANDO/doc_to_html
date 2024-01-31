def get_start_frame() -> int:
    """
     Get the start frame of the playback. This is used to determine when to
     start playing a frame from the user.


     Returns:
        int The frame number of the start frame of the playback or - 1 if there
        is no start frame
    """
    pass


def get_end_frame() -> int:
    """
     Get the end frame of the playback. This is used to determine when to stop
     playback after a frame has been played.


     Returns:
        int number of frames that have been played before the end of the
         current frame
    """
    pass


def get_character(character_name: str) -> str:
    """
    Get the character.

    Args:
        character_name: The name of the character

    Returns:
        The character.
    """
    pass


def get_controllers(character: str) -> list[str]:
    """
     Get all controllers connected to character. This is used to determine
     which transforms are connected to a character.

     Args:
        character: The character to check. Can be DAG or nurbs

     Returns:
        A list of objects
    """
    pass


def get_attributes(controller: str):
    """
     Get attributes of a controller. This is a helper function to get all
     attributes of a controller. The controller must exist before calling this
     function

     Args:
        controller: Name of the controller to get attributes of

     Returns:
        Dictionary of attributes or empty dictionary if there are no attributes
        in the controller. Attributes are returned as key - value pairs
    """
    pass


def build_data(character: str, frames: int = None) -> dict:
    """
     Builds and returns data to be sent to the character. This is a dictionary
     where keys are frames and values are controller attributes

     Args:
        character: Character to build data for
        frames: The frames to export. If not specified, exports all the
        timeline

     Returns:
        Dictionary with frames and controller attributes for the character.
        The key is frame and the value is a dictionary with controller
    """

    pass


def main(delivery_directory: str, animation_file: str,
         character_name: str, frames: list[int] = None) -> None:
    """
     Create and write data to delivery_directory. This is a script that will
     be run in the context of the script and will take care of the creation of
     the file and writing it to delivery_directory.

     Args:
        delivery_directory: Directory where we are going to store the data.
        animation_file: Name of the animation file that will be used to create
        the data.
        character_name: Name of the character for which we are going to create
        the data
        frames: The frames to export. If not specified, exports all the
        timeline
    """
    pass
