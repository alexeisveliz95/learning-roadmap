import tomllib
import os

# Default profile settings for password generation
DEFAULT_PROFILE = {
    "length": 8,
    "use_uppercase": True,
    "use_digits": True,
    "use_special_chars": True,
    "avoid_ambiguous": True,
    "minimum_uppercase": 1,
    "minimum_digits": 1,
    "minimum_special_chars": 1
}

# Load configuration from config.toml if exists, otherwise create a default config.toml
def load_profile(profile_name: str = "default") -> dict:
    """Loads a password generation profile from the config.toml file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.toml")
    
    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
            profile = config.get("profiles", {}).get(profile_name, {})
            # Return profile merged with defaults if any key is missing
            return {**DEFAULT_PROFILE, **profile} if profile else DEFAULT_PROFILE
    except FileNotFoundError:
        # If config.toml does not exist, create it with default profiles
        with open(config_path, "w") as f:
            f.write("[profiles.default]\n")
            for key, value in DEFAULT_PROFILE.items():
                if isinstance(value, bool):
                    f.write(f"{key} = {str(value).lower()}\n")
                else:
                    f.write(f"{key} = {value}\n")

if __name__ == "__main__":
    profile = load_profile("default")
    print(f"Loaded profile: {profile}")