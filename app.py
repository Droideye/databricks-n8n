from utils.jsrunner import NodeJsEntrypoint

# entrypoint for the n8n docker container
if __name__ == "__main__":
    entrypoint = NodeJsEntrypoint()
    entrypoint.with_npm_command("install n8n@latest").with_command("n8n").run()