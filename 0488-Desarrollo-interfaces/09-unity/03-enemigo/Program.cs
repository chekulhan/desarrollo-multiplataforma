// Vamos a añadir un enemigo quien ataca al player.

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

public class EnemyObject
{
    public string name;

    public EnemyObject(string name)
    {
        this.name = name;
        Debug.Log(name + " enemy has spawned!");
    }

    public void Attack(GameObject g)
    {
        g.TakeDamage(1);
        Debug.Log(g.name + " took a beating! Health now is " + g.health);
    }

}

// Simulate a MonoBehaviour with Update method
// MonoBehaviour provides many special methods that Unity automatically calls at specific times: Update, Start, FixedUpdate, ...

public class PlayerController
{
    public GameObject player;
    public EnemyObject enemy;

    public PlayerController()
    {
        player = new GameObject("Hero", 10);
        enemy = new EnemyObject("Enemy");
    }

    // Simulate Unity's Update loop
    public void Update(string command)
    {
        int OBJECTIVE = 5;

        if (command == "space")
        {
            player.TakeDamage(10);
        }
        else if (command == "a") {
            enemy.Attack(player);
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
            Console.WriteLine("input key:"+ input);
            if (input == "exit") break;

            controller.Update(input);
        }

        Debug.Log("Simulation ended.");
    }
}



