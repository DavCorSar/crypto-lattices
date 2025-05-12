class ClosestVectorHasNotBeenComputed(Exception):
    """
    This error can be thrown when a function that needs the
    closest vector `v` of the Babai algorithm is called and
    such vector has not been computed 
    """

    def __init__(self):
        self.message = "Please, first compute the closest vector \
using the compute_closest_vector method"
        super().__init__(self.message)
