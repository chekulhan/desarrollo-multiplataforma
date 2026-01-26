using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerController : MonoBehaviour
{

    public InputAction MoveAction;
    public InputAction Jump;
    private bool isGrounded = true;
    public float jumpForce = 5f;
    public float gravity = -9.8f;
    private float verticalVelocity = 0f;


    public int maxHealth = 5;
    int currentHealth;


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        MoveAction.Enable();
        Jump.Enable();

        currentHealth = maxHealth;

    }

    // Update is called once per frame
    void Update()
    {
        // Horizontal input
        Vector2 move = MoveAction.ReadValue<Vector2>();

        // Start from current position
        Vector2 position = (Vector2)transform.position;

        // Apply horizontal movement
        position += move * 0.1f;

        // Jump input
        if (Jump.WasPressedThisFrame() && isGrounded)
        {
            verticalVelocity = jumpForce;
            isGrounded = false;
        }

        // Apply gravity
        verticalVelocity += gravity * Time.deltaTime;
        position.y += verticalVelocity * Time.deltaTime;

        // Ground collision
        if (position.y <= 0f)
        {
            position.y = 0f;
            verticalVelocity = 0f;
            isGrounded = true;
        }

        // Apply final position
        transform.position = position;
    }

    public void ChangeHealth(int amount) {
        currentHealth = Mathf.Clamp(currentHealth + amount, 0, maxHealth);
        Debug.Log(currentHealth + "/" + maxHealth);
    }

}
