// Vamos a mover el player.
// Actividad: 
// Hacer un juego de movimiento de enemigos y player. Cuando se acerca y toca el enemigo al player, game over.

using System;

// Simulate Unity's Debug class
public static class Debug
{
    public static void Log(string message)
    {
        Console.WriteLine("[Debug] " + message);
    }
}

// Simulate a simple GameObject class
public class GameObject
{
    public string name;
    public int health;
    public int current_position;

    public GameObject(string name, int health)
    {
        this.name = name;
        this.health = health;
        this.current_position = 0;

        Debug.Log(name + " has spawned with " + health + " health!");
    }

    public void Move(int steps)
    {
        current_position += steps;
        Debug.Log(name + " took " + steps + " steps! Currently at " + current_position);
    }

    public void Draw()
    {
        int lineLength = 10; // total length of the line
            for (int i = 0; i < lineLength; i++)
            {
                if (i == current_position)
                    Console.Write("P"); // P = player
                else
                    Console.Write("-"); // empty space
            }
            Console.WriteLine(); // move to next line
                
    }

}



// Simulate a MonoBehaviour with Update method
// MonoBehaviour provides many special methods that Unity automatically calls at specific times: Update, Start, FixedUpdate, ...

public class PlayerController
{
    public GameObject player;
    

    public PlayerController()
    {
        player = new GameObject("Hero", 10);
        
    }

    // Simulate Unity's Update loop
    public void Update(string command)
    {
        int OBJECTIVE = 5;

        if (command == "space")
        {
            player.TakeDamage(10);
        }
        else if (command == "r") {
            player.Move(1);
        }


        if (player.current_position >= OBJECTIVE) {
            Debug.Log("Youve won!!!!!");
        }

        player.Draw(); // Pintamos de nuevo el player


    }
}

class Program
{
    static void Main()
    {
        PlayerController controller = new PlayerController();

        Debug.Log("Type 'space' and hit enter to deal damage. Type 'exit' to quit.");

        string input;
        while (true)
        {
            input = Console.ReadLine(); 
            Console.WriteLine("input key:"+ input);
            if (input == "exit") break;

            controller.Update(input);
        }

        Debug.Log("Simulation ended.");
    }
}


// para usar flechas, hay que usar
// ConsoleKeyInfo keyInfo = Console.ReadKey(true);
// if (keyInfo.Key == ConsoleKey.RightArrow)
