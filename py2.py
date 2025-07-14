import requests

access_token = "AQWh02OzNTtl7vqcXk5TRziyYwEZPs_Iz34xC3cb2oQwIuk0PfCLzGeFnhVxo0XDx7y8S3jVBCG4kpHo_REvC4Mmr-V4IB5NREUmRcip1DI64kDVSni-N0sR-8LDvbaB83OxM2zIH_rah5GlJP_h2a5vg1cKsg9C3GQjgXwgJzJ3TuMDfO3l-cG6FGR9QaEzWGTHZdTUu7Neguy5acLbOwjklrIQ4jkuzdcSU2ySJBCoru6za-inKhSKuGhyJVO8NdrFNznX6JYo2BB5gNBBEKxcnF_AUJza-uH7nwBIHmoHvss6lSS6yS54GaQe1aJvFjaAL2xVLA8F9b5QSUJw5D0XMrg3Aw"

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get("https://api.linkedin.com/v2/me", headers=headers)

print(response.status_code)
print(response.json())
