import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from view.menu import Menu

if __name__ == "__main__":
    app = Menu()
    app.mainloop()