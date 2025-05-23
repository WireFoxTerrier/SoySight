import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import time

def print_welcome():
    console = Console()

    # 生成 ASCII 大字标题
    ascii_title = pyfiglet.figlet_format("SoySight", font="slant")

    # 显示 ASCII 标题的“爬行”打印效果
    for line in ascii_title.split("\n"):
        console.print(f"[bold yellow]{line}[/bold yellow]")
        time.sleep(0.2)

    # 正文内容，使用 append 构造
    intro_text = Text()
    intro_text.append("\n")
    intro_text.append(" Welcome to ", style="white")
    intro_text.append("SoySight", style="bold green")
    intro_text.append(" - U.S. Soybean Export Trend Explorer\n", style="white")
    intro_text.append(" Track weekly export volumes and highlight key crop years with ease.\n", style="white")
    intro_text.append("\n", style="white")
    intro_text.append(" How it works:\n", style="bold white")
    intro_text.append(" Simply enter the crop years you're interested in, and SoySight will\n", style="white")
    intro_text.append(" visualize weekly accumulated soybean exports using official USDA data.\n", style="white")
    intro_text.append(" Highlight any specific years to compare trends more effectively.\n", style="white")
    intro_text.append("\n", style="white")
    intro_text.append(" Version: ", style="white")
    intro_text.append("v1.0", style="bold white")
    intro_text.append("   🌻  Built with Python\n", style="yellow")

    # 创建 Panel，设置边框颜色和 padding
    panel = Panel(intro_text, border_style="green", padding=(1, 4))

    # 顶部和底部的 🌱 emoji 边框
    emoji_bar = "🌱" * 60
    console.print("\n" + emoji_bar, style="green")
    console.print(panel)
    console.print(emoji_bar + "\n", style="green")