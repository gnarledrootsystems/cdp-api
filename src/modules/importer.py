import click

def importer(app):
    # @click.option("--my-option")
    @app.cli.command("importer")
    def importer():
        print("Running importer...")
        
    return app

def load_files():
    print("Loading Files...")