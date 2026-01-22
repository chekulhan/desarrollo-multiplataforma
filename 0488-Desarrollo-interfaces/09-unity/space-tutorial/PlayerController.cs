using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerController : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

        //Vector3 mousePos = Mouse.current.position.value;
        Vector3 mousePos = Camera.main.ScreenToWorldPoint(Mouse.current.position.value);

        if (Mouse.current.leftButton.isPressed) {
            Debug.Log($"Mouse Position: {mousePos}");
            Vector2 direction = mousePos - transform.position;
            Debug.Log(direction);
            transform.up = direction;
        }
    }
}

