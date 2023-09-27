using System;
using GeometryLibrary;

/// <summary>
/// Это главный класс приложения, который предоставляет возможность пользователю вводить данные
/// и выполнять операции с квадратом.
/// </summary>
class Program
{
    /// <summary>
    /// Точка входа в приложение.
    /// </summary>
    static void Main()
    {
        Console.WriteLine("Введите длину стороны квадрата:");
        double sideLength = double.Parse(Console.ReadLine());

        Console.WriteLine("Введите x:");
        double sx = double.Parse(Console.ReadLine());
        Console.WriteLine("Введите y:");
        double sy= double.Parse(Console.ReadLine());
        // Создаем экземпляр квадрата на основе введенной длины стороны.
        Square square;

        try
        {
            square = new Square(sideLength, sx, sy);
            Console.WriteLine($"Площадь квадрата: {square.CalculateArea()}");
            Console.WriteLine($"Периметр квадрата: {square.CalculatePerimeter()}");

            Console.WriteLine("Введите координаты точки для проверки ее принадлежности квадрату:");
            Console.Write("X: ");
            double x = double.Parse(Console.ReadLine());
            Console.Write("Y: ");
            double y = double.Parse(Console.ReadLine());

            if (square.ContainsPoint(x, y))
            {
                Console.WriteLine($"Точка ({x}, {y}) принадлежит квадрату.");
            }
            else if (square.IsOnBoundary(x, y))
            {
                Console.WriteLine($"Точка ({x}, {y}) находится на границе квадрата.");
            }
            else
            {
                Console.WriteLine($"Точка ({x}, {y}) не принадлежит квадрату.");
            }
        }
        catch {
            Console.WriteLine("Недопустимая длина стороны квадрата.");
        }
    }
}
