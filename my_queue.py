# encoding uft-8
"""
This module provide special Queue data structure

Used in Python training session

If you want to follow this training session please do not read the following file
"""

__author__  = "Yannis Van Achter <yannis.vanachter@student.unamur.be>"
__date__    = "24 february 2023"
__version__ = "1.0.0"






































class MyQueue:
    def __init__(self, *args, typed: type = None, size: int = None):
        """creat queue data structure

        Create Queue data structure with type and size options.

        Args:
        -----
            typed (type, optional): type of data stored, if None we can add any type of data to the queue. Defaults to None.
            size (int, optional): maximum size of the queue, if None we can add infinit values. Defaults to None.
        """
        # init object variables
        self._queue = []

        if typed != None and not callable(typed):
            raise TypeError("Typed must be an object")
        self._typed = typed

        if size != None and (not isinstance(size, int)) or size <= 0:
            raise ValueError("Size must be a strict positive integer")
        self._size = size

        # add data to queue
        r = self._set_queue(*args)

        if r > size or r < 0:
            raise Exception("Queue wrongly init")

    def _get_type(self):
        """Get queue type

        Returns:
        --------
            type: type of object allow in the queue
        """
        return self._typed

    def _set_type(self, value):
        """set Queue type after instanciation 

        Set queue type after instanciation if it is None at this time or does not contain any object

        Args:
        -----
            value (type): Type as int, str, float ... (any object you want)

        Raises:
        -------
            Exception: if it is typed already or Queue contain at least one element
        """
        if self._typed is None and len(self._queue) == 0:
            raise Exception("You cannot change the type of an Queue instance")
        self._typed = value

    typed = property(_get_type, _set_type)

    def _get_size(self):
        """get size of the Queue

        Get current size if there is no limit, else the limit

        Returns:
        --------
            int: size of the Queue 
        """
        return self._size if self._size != None else len(self._queue)

    def _set_size(self, value):
        """set a maximum size at the Queue

        Set maximum size at the current Queue instance

        Args:
        -----
            value (int): new maximum size (strictly positive and greater than current size)

        Raises:
        -------
            TypeError: if value is not an integer
            ValueError: if value is lower or equal to zero OR it is lower than current len()
        """
        if isinstance(value, int):
            raise TypeError("value must be an positive integer")
        if value <= 0 or value < len(self._queue):
            raise ValueError(
                "You cannot change the size of an Queue instance, it is already to big or is negative"
            )
        self._size = value
        
    size = property(_get_size, _set_size)

    def _get_queue(self):
        """Return first element of the Queue

        Returns:
        --------
            object: the first object in the Queue (if Queue is typed it respect the type of the Queue)
        """
        if len(self._queue) == 0:
            return None
        return self._queue.pop(0)

    def _set_queue(self, *values):
        """Add value at the end of the Queue

        Raises:
        -------
            TypeError: if Queue is typed and one of the value does not respect this type casting

        Returns:
        --------
            int: current len of the Queue, -1 otherwise.
        """
        for val in values:
            if self._size == None or len(self._queue) < self._size:
                if self._typed == None:
                    self._queue.append(val)
                else:
                    if self._typed == type(val):
                        self._queue.append(val)
                    else:
                        raise TypeError(
                            f"You formated the queue to add only {self.typed} elements"
                        )
            else:
                return -1

        return len(self._queue)

    queue = property(_get_queue, _set_queue)

    def __len__(self):
        """return the current size of the queue

        Returns:
        --------
            int: size of queue >= 0
        """
        return len(self._queue)

    def enqueue(self, *values):
        """Add values in the Queue
        
        Args:
        -----
            values (list): values to enqueue
        
        Raises:
        -------
            TypeError: if Queue is typed and one of the value does not respect this type casting
        """
        self._set_queue(self, *values)

    def dequeue(self):
        """Return the first value of the Queue

        Returns:
            object: first value of the Queue (if the Queue is empty, return None)
        """
        return self._get_queue()
