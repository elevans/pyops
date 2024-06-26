import imglyb
import numpy as np

from pysjo.java import imglib


def imglib_to_numpy(
    rai: "imglib.RandomAccessibleInterval", dtype="float64"
) -> np.ndarray:
    """Convert an ImgLib2 RandomAccessibleInterval to NumPy array.

    :param rai: Input RandomAccessibleInterval (RAI)
    :param dtype: dtype for output NumPy array (default=float64)
    :return: A NumPy array with the copied data and dtype
    """
    # create empty NumPy array
    shape = list(rai.dimensionsAsLongArray())
    shape.reverse()  # XY -> row, col
    narr = np.zeros(shape, dtype=dtype)

    # create RAI reference with imglyb and compy data
    imglib.ImgUtil.copy(rai, imglyb.to_imglib(narr))

    return narr


def mesh_to_ndarray(mesh: "imglib.Mesh") -> np.ndarray:
    """Convert an imglib2 mesh into a numpy array of trianges.

    :param mesh: An imglib2 Mesh
    :return: A NumPy array of triangles
    """
    tri_verts = []
    for t in mesh.triangles():
        verts = ((t.v0xf(), t.v0yf(), t.v0zf()),
                 (t.v1xf(), t.v1yf(), t.v1zf()),
                 (t.v2xf(), t.v2yf(), t.v2zf()))
        tri_verts.append(np.array(verts))

    return np.array(tri_verts)


def numpy_to_imglib(narr: np.ndarray) -> "imglib.RandomAccessibleInterval":
    """Convert a NumPy image to an ImgLib2 RandomAccessibleInterval.

    :param narr: Input NumPy array
    :return: An ImgLib2 RandomAccessibleInterval (reference)
    """
    return imglyb.to_imglib(narr)
