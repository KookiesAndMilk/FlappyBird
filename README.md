# FlappyBird
Es un proyecto en pygame del juego Flappy Bird

# Flappy Bird en Pygame

Este proyecto es una implementación del juego clásico **Flappy Bird** en Python, utilizando la biblioteca **Pygame**. El objetivo del juego es que el jugador controle al pájaro para evitar obstáculos y ganar puntos.

## Requisitos

Asegúrate de tener instalados los siguientes componentes:

- **Python 3.x**
- **Pygame** (para instalarlo, ejecuta `pip install pygame` en la terminal)

## Archivos necesarios

Asegúrate de incluir los siguientes archivos en la misma carpeta que el script:

1. **sprites/**
   - `background-night.png`: fondo del juego.
   - `base.png`: imagen para el suelo.
   - `pipe-brown.png`: imagen de las tuberías.
   - `pinkbird-downflap.png`, `pinkbird-midflap.png`, `pinkbird-upflap.png`: imágenes de las posiciones del pájaro.
   - `message.png`: imagen para la pantalla de "Game Over".

2. **audio/**
   - `wing.wav`: sonido al saltar.
   - `hit.wav`: sonido al colisionar.
   - `point.wav`: sonido al obtener puntos.

## Estructura del código

### Funciones principales

- **draw_floor**: Dibuja el suelo en el juego y realiza el desplazamiento horizontal.
- **create_pipe**: Genera tuberías con una posición aleatoria y las devuelve como objetos `Rect`.
- **move_pipes**: Mueve las tuberías de izquierda a derecha.
- **draw_pipes**: Dibuja las tuberías en la pantalla y las voltea si es necesario.
- **check_collision**: Verifica si el pájaro ha colisionado con una tubería o ha tocado los bordes.
- **rotate_bird**: Rota el pájaro para simular el movimiento de subida o caída.
- **bird_animation**: Alterna las posiciones del pájaro para crear el efecto de "flap".
- **score_display**: Muestra la puntuación en pantalla tanto durante el juego como en el estado de "Game Over".
- **update_score**: Actualiza la puntuación máxima (high score).

### Variables del juego

- **gravity**: La velocidad de caída del pájaro.
- **bird_movement**: Movimiento vertical del pájaro.
- **jump_strength**: La fuerza del salto al presionar la barra espaciadora.
- **score y high_score**: Variables para la puntuación y puntuación máxima.

### Ciclo principal del juego

1. **Eventos**: Controla el salto del pájaro, el reinicio del juego y el cierre de la ventana.
2. **Estado activo**: Controla el movimiento del pájaro, dibuja las tuberías y verifica las colisiones.
3. **Pantalla de "Game Over"**: Se muestra al perder el juego, mostrando la puntuación final y el puntaje máximo.

## Cómo ejecutar el juego

1. Clona el repositorio en tu computadora o descarga el archivo `.py`.
2. Navega al directorio del proyecto en la terminal.
3. Ejecuta el archivo de juego:

   ```bash
   python flappy_bird.py
   ```

4. **Instrucciones de juego**:
   - Presiona la barra espaciadora para hacer que el pájaro salte.
   - Evita chocar con las tuberías o el suelo.
   - Intenta obtener la mayor cantidad de puntos posibles.

## Personalización

Para ajustar el juego, puedes modificar los siguientes parámetros en el código:

- **Gravedad** (`gravity`): Para hacer que el pájaro caiga más rápido o más lento.
- **Fuerza del salto** (`jump_strength`): Para ajustar la altura del salto.
- **Distancia entre tuberías** (`pipe_height`): Para hacer el juego más difícil o fácil cambiando las alturas posibles de las tuberías.

## Créditos

Inspirado en el juego original de **Flappy Bird**. Implementado con **Python** y **Pygame** por Melanie Irigoyen.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver los detalles en el archivo LICENSE.


