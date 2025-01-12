import os
from solutions.tarea1_solucion import detect_edges

def test_detect_edges():
    input_image = "assignments/task1/input_data/image1.jpg"
    output_image = "assignments/task1/output_data/image1.jpg"
    detect_edges(input_image, output_image)

    assert os.path.exists(output_image), "La imagen de salida no se generó."
