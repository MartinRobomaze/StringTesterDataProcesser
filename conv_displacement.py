max_displacement_raw = 0.0058162267839687
min_displacement_raw = 0.0320625610948191

min_displacement_mm = 0
max_displacement_mm = 1


def conv_displacement_to_mm(x):
    return (x - min_displacement_raw) * (max_displacement_mm - min_displacement_mm) / (max_displacement_raw - min_displacement_raw) + min_displacement_mm


