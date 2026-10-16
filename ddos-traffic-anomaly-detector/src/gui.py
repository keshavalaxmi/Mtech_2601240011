
import csv
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from src.anomaly_detector import detect_anomalies

# DDoS dashboard theme
BG = "#090D1A"
PANEL = "#17182B"
PANEL2 = "#211D36"
PURPLE = "#B7A0FF"
PINK = "#FF4D8D"
GREEN = "#72F1B8"
WHITE = "#F4F1FF"
MUTED = "#A7A8C7"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "traffic.csv"
OUTPUT_FILE = BASE_DIR / "output" / "detection_results.csv"


class DDoSDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("DDoS Traffic Anomaly Detector")
        self.root.geometry("1100x760")
        self.root.minsize(850, 650)
        self.root.configure(bg=BG)

        self.results = []
        self.analysis_runs = 0

        self.setup_styles()
        self.build_header()
        self.build_metrics()
        self.build_graph()
        self.build_table()
        self.build_footer()

        self.root.after(250, self.analyze)

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background=PANEL,
            foreground=WHITE,
            fieldbackground=PANEL,
            rowheight=28,
            font=("Consolas", 10),
        )
        style.configure(
            "Treeview.Heading",
            background=PANEL2,
            foreground=PURPLE,
            font=("Consolas", 10, "bold"),
        )
        style.map(
            "Treeview",
            background=[("selected", "#393054")],
            foreground=[("selected", WHITE)],
        )

    def build_header(self):
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=22, pady=(18, 12))

        left = tk.Frame(header, bg=BG)
        left.pack(side="left", fill="x", expand=True)

        tk.Label(
            left,
            text="◈ NETWORK SECURITY / TRAFFIC ANALYSIS",
            bg=BG,
            fg=PURPLE,
            font=("Consolas", 10, "bold"),
        ).pack(anchor="w")

        tk.Label(
            left,
            text="DDoS Traffic Anomaly Detector",
            bg=BG,
            fg=WHITE,
            font=("Segoe UI", 23, "bold"),
        ).pack(anchor="w", pady=(5, 2))

        tk.Label(
            left,
            text="SLIDING-WINDOW BASELINE  •  ANOMALY MONITORING",
            bg=BG,
            fg=MUTED,
            font=("Consolas", 9),
        ).pack(anchor="w")

        self.status = tk.Label(
            header,
            text="● READY",
            bg=PANEL2,
            fg=PURPLE,
            font=("Consolas", 10, "bold"),
            padx=14,
            pady=10,
        )
        self.status.pack(side="right", anchor="n")

    def build_metrics(self):
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="x", padx=22, pady=7)

        self.cards = {}

        for title, key, color in [
            ("TOTAL SAMPLES", "total", PURPLE),
            ("ANOMALIES", "anomalies", PINK),
            ("NORMAL SAMPLES", "normal", GREEN),
            ("PEAK PACKETS", "peak", PURPLE),
        ]:
            card = tk.Frame(
                frame,
                bg=PANEL,
                highlightbackground=PANEL2,
                highlightthickness=1,
            )
            card.pack(
                side="left",
                fill="both",
                expand=True,
                padx=(0, 9),
            )

            tk.Label(
                card,
                text=title,
                bg=PANEL,
                fg=MUTED,
                font=("Consolas", 9, "bold"),
            ).pack(anchor="w", padx=13, pady=(11, 3))

            value = tk.Label(
                card,
                text="—",
                bg=PANEL,
                fg=color,
                font=("Consolas", 22, "bold"),
            )
            value.pack(anchor="w", padx=13, pady=(0, 11))
            self.cards[key] = value

    def build_graph(self):
        panel = tk.Frame(
            self.root,
            bg=PANEL,
            highlightbackground=PANEL2,
            highlightthickness=1,
        )
        panel.pack(
            fill="both",
            expand=True,
            padx=22,
            pady=9,
        )

        top = tk.Frame(panel, bg=PANEL)
        top.pack(fill="x", padx=15, pady=(12, 3))

        tk.Label(
            top,
            text="PACKET TRAFFIC",
            bg=PANEL,
            fg=WHITE,
            font=("Consolas", 11, "bold"),
        ).pack(side="left")

        tk.Label(
            top,
            text="━ TRAFFIC    ● DETECTED ANOMALY",
            bg=PANEL,
            fg=PURPLE,
            font=("Consolas", 9),
        ).pack(side="right")

        self.canvas = tk.Canvas(
            panel,
            bg=PANEL,
            height=220,
            highlightthickness=0,
        )
        self.canvas.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=8,
        )
        self.canvas.bind(
            "<Configure>",
            lambda event: self.draw_graph(),
        )

    def build_table(self):
        panel = tk.Frame(self.root, bg=BG)
        panel.pack(fill="x", padx=22, pady=(3, 8))

        tk.Label(
            panel,
            text="ANALYSIS RESULTS",
            bg=BG,
            fg=WHITE,
            font=("Consolas", 11, "bold"),
        ).pack(anchor="w", pady=(0, 7))

        columns = (
            "timestamp",
            "packets",
            "baseline",
            "average",
            "status",
        )

        self.table = ttk.Treeview(
            panel,
            columns=columns,
            show="headings",
            height=5,
        )

        headings = {
            "timestamp": "SAMPLE",
            "packets": "PACKETS",
            "baseline": "PREVIOUS BASELINE",
            "average": "WINDOW AVERAGE",
            "status": "DETECTION RESULT",
        }

        for column in columns:
            self.table.heading(column, text=headings[column])
            self.table.column(column, width=150, anchor="center")

        self.table.tag_configure("anomaly", foreground=PINK)
        self.table.tag_configure("normal", foreground=GREEN)
        self.table.pack(fill="x")

    def build_footer(self):
        footer = tk.Frame(self.root, bg=BG)
        footer.pack(fill="x", padx=22, pady=(3, 16))

        self.footer = tk.Label(
            footer,
            text="DATA SOURCE: data/traffic.csv",
            bg=BG,
            fg=MUTED,
            font=("Consolas", 9),
        )
        self.footer.pack(side="left")

        self.export_button = tk.Button(
            footer,
            text="↓  EXPORT RESULTS",
            command=self.export_results,
            bg=GREEN,
            fg=BG,
            activebackground=PURPLE,
            activeforeground=BG,
            relief="flat",
            cursor="hand2",
            font=("Consolas", 10, "bold"),
            padx=14,
            pady=9,
        )
        self.export_button.pack(side="right", padx=(8, 0))

        self.analyze_button = tk.Button(
            footer,
            text="↻  ANALYZE TRAFFIC",
            command=self.analyze,
            bg=PURPLE,
            fg=BG,
            activebackground=PINK,
            activeforeground=BG,
            relief="flat",
            cursor="hand2",
            font=("Consolas", 10, "bold"),
            padx=16,
            pady=9,
        )
        self.analyze_button.pack(side="right")

    def load_packet_counts(self):
        if not DATA_FILE.exists():
            raise FileNotFoundError(
                f"Dataset not found:\n{DATA_FILE}"
            )

        with DATA_FILE.open(
            "r",
            newline="",
            encoding="utf-8-sig",
        ) as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        if not rows:
            raise ValueError("traffic.csv is empty.")

        packet_counts = []
        accepted_columns = {
            "packets",
            "packet_count",
            "traffic",
            "traffic_count",
            "packets_count",
            "count",
            "value",
        }

        for row in rows:
            value = None

            for key, item in row.items():
                if key and key.strip().lower() in accepted_columns:
                    value = item
                    break

            if value is None:
                raise ValueError(
                    "Traffic column not found. CSV columns: "
                    + ", ".join(str(key) for key in row.keys())
                )

            try:
                count = int(float(value))
            except (TypeError, ValueError):
                raise ValueError(
                    f"Invalid packet count in CSV: {value}"
                ) from None

            if count < 0:
                raise ValueError(
                    f"Packet count cannot be negative: {count}"
                )

            packet_counts.append(count)

        return packet_counts

    def analyze(self):
        self.analyze_button.config(state="disabled")
        self.status.config(text="● ANALYZING", fg=PURPLE)
        self.footer.config(text="Loading data and analyzing traffic...")
        self.root.update_idletasks()

        try:
            packet_counts = self.load_packet_counts()
            new_results = detect_anomalies(packet_counts)

            if not new_results:
                raise ValueError("No traffic samples were analyzed.")

            anomaly_count = sum(
                1 for result in new_results if result["anomaly"]
            )
            normal_count = len(new_results) - anomaly_count

            self.results = new_results

            self.cards["total"].config(text=str(len(new_results)))
            self.cards["anomalies"].config(text=str(anomaly_count))
            self.cards["normal"].config(text=str(normal_count))
            self.cards["peak"].config(text=f"{max(packet_counts):,}")

            self.update_table()
            self.draw_graph()

            self.analysis_runs += 1

            if anomaly_count:
                self.status.config(
                    text="● ANOMALIES FOUND",
                    fg=PINK,
                )
            else:
                self.status.config(
                    text="● NO ANOMALIES",
                    fg=GREEN,
                )

            self.footer.config(
                text=(
                    f"DATA: traffic.csv  |  "
                    f"{len(new_results)} samples analyzed  |  "
                    f"Run #{self.analysis_runs} complete"
                )
            )

        except Exception as error:
            self.status.config(text="● ERROR", fg=PINK)
            self.footer.config(text="Analysis failed.")
            messagebox.showerror("Analysis Error", str(error))

        finally:
            self.analyze_button.config(state="normal")

    def export_results(self):
        if not self.results:
            messagebox.showwarning(
                "No Results",
                "Please analyze the traffic before exporting results.",
            )
            return

        fieldnames = [
            "timestamp",
            "packets",
            "baseline",
            "anomaly",
            "window_average",
        ]

        try:
            OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

            with OUTPUT_FILE.open(
                "w",
                newline="",
                encoding="utf-8",
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames,
                )
                writer.writeheader()
                writer.writerows(self.results)

            self.footer.config(
                text="RESULTS EXPORTED: output/detection_results.csv"
            )

            messagebox.showinfo(
                "Export Successful",
                f"Results saved successfully to:\n{OUTPUT_FILE}",
            )

        except OSError as error:
            messagebox.showerror(
                "Export Error",
                f"Could not save results:\n{error}",
            )

    def update_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

        for result in self.results:
            anomaly = result["anomaly"]

            self.table.insert(
                "",
                "end",
                values=(
                    result["timestamp"],
                    result["packets"],
                    f'{result["baseline"]:.2f}',
                    f'{result["window_average"]:.2f}',
                    "ANOMALY" if anomaly else "NORMAL",
                ),
                tags=("anomaly" if anomaly else "normal",),
            )

    def draw_graph(self):
        canvas = self.canvas
        canvas.delete("all")

        if not self.results:
            canvas.create_text(
                300,
                100,
                text="Click ANALYZE TRAFFIC to load data",
                fill=MUTED,
                font=("Consolas", 11),
            )
            return

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        if width < 100 or height < 80:
            return

        left = 60
        right = width - 25
        top = 28
        bottom = height - 35

        values = [result["packets"] for result in self.results]
        maximum = max(max(values) * 1.15, 1)
        denominator = max(len(values) - 1, 1)

        for step in range(5):
            y = bottom - (bottom - top) * step / 4
            label = maximum * step / 4

            canvas.create_line(
                left,
                y,
                right,
                y,
                fill="#34304A",
                dash=(3, 5),
            )
            canvas.create_text(
                left - 8,
                y,
                text=f"{label:.0f}",
                fill=MUTED,
                anchor="e",
                font=("Consolas", 8),
            )

        points = []
        anomaly_points = []

        for index, result in enumerate(self.results):
            x = left + (right - left) * index / denominator
            y = bottom - (
                (bottom - top) * result["packets"] / maximum
            )

            points.extend([x, y])

            if result["anomaly"]:
                anomaly_points.append((x, y, result))

        if len(points) >= 4:
            canvas.create_line(
                *points,
                fill=PURPLE,
                width=2.5,
            )

        for x, y, result in anomaly_points:
            canvas.create_oval(
                x - 7,
                y - 7,
                x + 7,
                y + 7,
                fill=PINK,
                outline=WHITE,
                width=2,
            )

            label_y = max(top + 9, y - 19)

            canvas.create_text(
                x,
                label_y,
                text=str(result["packets"]),
                fill=PINK,
                font=("Consolas", 9, "bold"),
            )

        canvas.create_text(
            right,
            top - 12,
            text=f"{len(anomaly_points)} anomalies detected",
            fill=PINK if anomaly_points else GREEN,
            anchor="ne",
            font=("Consolas", 9, "bold"),
        )

        canvas.create_text(
            left,
            height - 10,
            text="SAMPLE 1",
            fill=MUTED,
            anchor="w",
            font=("Consolas", 8),
        )

        canvas.create_text(
            right,
            height - 10,
            text=f"SAMPLE {len(self.results)}",
            fill=MUTED,
            anchor="e",
            font=("Consolas", 8),
        )


def main():
    root = tk.Tk()
    DDoSDashboard(root)
    root.mainloop()


if __name__ == "__main__":
    main()
