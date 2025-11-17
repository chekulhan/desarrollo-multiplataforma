
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

    public GameObject(string name, int health)
    {
        this.name = name;
        this.health = health;
        Debug.Log(name + " has spawned with " + health + " health!");
    }

    public void TakeDamage(int damage)
    {
        health -= damage;
        Debug.Log(name + " took " + damage + " damage! Health is now " + health);
        if (health <= 0)
        {
            Debug.Log(name + " has been defeated!");
        }
    }
}

// Simulate a MonoBehaviour with Update method
public class PlayerController
{
    public GameObject player;

    public PlayerController()
    {
        player = new GameObject("Hero", 100);
    }

    // Simulate Unity's Update loop
    public void Update(string command)
    {
        if (command == "space")
        {
            player.TakeDamage(10);
        }
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
            if (input == "exit") break;

            controller.Update(input);
        }

        Debug.Log("Simulation ended.");
    }
}
