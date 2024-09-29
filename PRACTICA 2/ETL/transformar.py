def transformar_info(datos):
    print("Transformar")
    
    # Asegúrate de que los datos no estén vacíos
    if datos.empty:
        raise ValueError("No hay datos para transformar")

    # Eliminar filas donde 'Rating' es NaN (si es necesario)
    datos = datos.dropna(subset=['Course Title','Rating', 'Level', 'Duration', 'Schedule', 'Review', 'What you will learn', 'Skill gain', 'Modules', 'Instructor', 'Offered By', 'Keyword', 'Course Url'])

    return datos
