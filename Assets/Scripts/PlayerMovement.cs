using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public float moveSpeed = 5f;  // Adjust speed in Inspector
    private Rigidbody2D rb;
    private Vector2 movementInput;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // Get movement input from Arrow Keys or WASD
        float moveX = Input.GetAxisRaw("Horizontal");
        float moveY = Input.GetAxisRaw("Vertical");

        movementInput = new Vector2(moveX, moveY).normalized;

    }

    void FixedUpdate()
    {
        // Apply movement using Rigidbody2D to obey physics
        //rb.linearVelocity = movementInput * moveSpeed;
        rb.linearVelocity = Vector2.Lerp(rb.linearVelocity, movementInput * moveSpeed, Time.fixedDeltaTime * 10);


    }
}
