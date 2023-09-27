using System;

namespace GeometryLibrary
{
    /// <summary>
    /// Представляет квадрат с указанной длиной стороны.
    /// </summary>
    public class Square
    {
        private double sideLength;
        private double x;
        private double y;

        /// <summary>
        /// Инициализирует новый экземпляр класса Square с указанной длиной стороны.
        /// </summary>
        /// <param name="sideLength">Длина стороны квадрата.</param>
        public Square(double sideLength, double x, double y)
        {
            this.sideLength = sideLength;
            this.x = x;
            this.y = y;
            if (!IsValid())
            {
                throw new InvalidOperationException("Квадрат недопустимой формы");
            }
        }

        /// <summary>
        /// Проверяет, является ли квадрат допустимой формы.
        /// </summary>
        /// <returns>True, если квадрат допустимой формы, в противном случае - False.</returns>
        public bool IsValid()
        {
            return sideLength > 0;
        }

        /// <summary>
        /// Вычисляет площадь квадрата.
        /// </summary>
        /// <returns>Площадь квадрата.</returns>
        /// <exception cref="InvalidOperationException">Вызывается, если квадрат недопустимой формы.</exception>
        public double CalculateArea()
        {
            return sideLength * sideLength;
        }

        /// <summary>
        /// Вычисляет периметр квадрата.
        /// </summary>
        /// <returns>Периметр квадрата.</returns>
        /// <exception cref="InvalidOperationException">Вызывается, если квадрат недопустимой формы.</exception>
        public double CalculatePerimeter()
        {
            return 4 * sideLength;
        }

        /// <summary>
        /// Проверяет, содержит ли квадрат указанную точку.
        /// </summary>
        /// <param name="x">Координата X точки.</param>
        /// <param name="y">Координата Y точки.</param>
        /// <returns>True, если точка находится внутри квадрата, в противном случае - False.</returns>
        /// <exception cref="InvalidOperationException">Вызывается, если квадрат недопустимой формы.</exception>
        public bool ContainsPoint(double x, double y)
        {
            return x-this.x > 0 && x-this.x < sideLength && y-this.y > 0 && y-this.y < sideLength;
        }

        /// <summary>
        /// Проверяет, находится ли точка на границе квадрата.
        /// </summary>
        /// <param name="x">Координата X точки.</param>
        /// <param name="y">Координата Y точки.</param>
        /// <returns>True, если точка находится на границе квадрата, в противном случае - False.</returns>
        /// <exception cref="InvalidOperationException">Вызывается, если квадрат недопустимой формы.</exception>
        public bool IsOnBoundary(double x, double y)
        {
            return (x-this.x == 0 || x - this.x == sideLength) && (y - this.y >= 0 && y - this.y <= sideLength) ||
                   (y - this.y == 0 || y - this.y == sideLength) && (x - this.x >= 0 && x - this.x <= sideLength);
        }
    }
}
