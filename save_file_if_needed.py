def save_file_if_needed(fname, fcontent):
    # Import modules ...
    import os

    # Check that the content is one of the two types allowed in Python 3 and set
    # the file access mode ...
    if isinstance(fcontent, bytes):
        mode = "b"
    elif isinstance(fcontent, str):
        mode = "t"
    else:
        raise TypeError("\"fcontent\" is an unexpected type")

    # Initizalize trigger ...
    save = False

    # Check if the file does not exist ...
    if not os.path.exists(fname):
        save = True

        # Check if the target directory does not exist ...
        if not os.path.exists(os.path.dirname(fname)):
            # Make directory ...
            os.makedirs(os.path.dirname(fname))
    else:
        # Check the old content ...
        if open(fname, "r" + mode).read() != fcontent:
            save = True

    # Save the file if needed ...
    if save:
        open(fname, "w" + mode).write(fcontent)
