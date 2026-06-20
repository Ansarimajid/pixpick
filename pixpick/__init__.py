from pixpick.selectors.box import BoxSelector, SelectionCancelled
from pixpick.core.selection import Box
from pixpick.utils import ImageSource


def box(source: ImageSource, title: str = "pixpick") -> Box:
    """
    Open an interactive window on `source`, let the user drag a box,
    and return a Box selection object.

    Parameters
    ----------
    source : str | Path | np.ndarray
        Image file path or BGR numpy array.
    title : str
        Window title shown to the user.

    Returns
    -------
    Box

    Raises
    ------
    SelectionCancelled
        If the user pressed Esc.

    Example
    -------
    >>> region = pixpick.box("frame.jpg")
    >>> region.xyxy
    [120, 80, 640, 480]
    >>> model.predict("frame.jpg", **region.to_yolo())
    """
    return BoxSelector().select(source, title=title)


def load(path: str) -> Box:
    """Load a previously saved Box from a JSON file."""
    return Box.load(path)


__all__ = [
    "box",
    "load",
    "Box",
    "BoxSelector",
    "SelectionCancelled",
]