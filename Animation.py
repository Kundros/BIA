import io
from math import ceil

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# Disable warning for generated graphs
plt.rcParams.update({'figure.max_open_warning': 0})

class Animation:
    def __init__(self, data, lB, uB, seg, func, name,
                 wire_width = 0.5,
                 wired=True,
                 rotation_deg_per_frame=0,
                 duration=25
                 ):
        self.data = data
        self.frames = []
        self.add_angle = 0

        # create mesh with seg * seg points
        self.X = np.arange(lB, uB, (uB - lB) / seg)
        self.Y = np.arange(lB, uB, (uB - lB) / seg)
        self.X, self.Y = np.meshgrid(self.X, self.Y)

        # calculate all Z values
        self.Z = func([self.X, self.Y])

        self.func = func
        self.rotation_deg_per_frame = rotation_deg_per_frame
        self.duration = duration

        self.wire_width = wire_width
        self.wired = wired

        self.name = name
        self.path = name + ".gif"

    ### Generates blob containing the image of graph (frame)
    def make_frame_3d(self, points = None):
        fig = plt.figure(figsize=plt.figaspect(1))
        ax = fig.add_subplot(1, 1, 1, projection='3d', computed_zorder=True)
        ax.view_init(45, -45 + self.add_angle, 0)

        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Plot either wireframe or surface of the Function (X, Y, Z)
        if self.wired:
            ax.plot_wireframe(self.X, self.Y, self.Z, rstride=1, cstride=1, color="blue", linewidth=self.wire_width)
        else:
            ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap="turbo", linewidth=0)

        # plot the point if is not a None
        if points is not None:
            for point in points:
                ax.plot(point[0], point[1], point[2], 'o-', color='red', markersize=4, dash_capstyle="projecting", antialiased=False, zorder=10)
                # print text with Z value
                ax.text(point[0], point[1], point[2] , str(round(point[2], 2)), horizontalalignment='center', verticalalignment='top', bbox=dict(facecolor='orange', alpha=0.4), zorder=11)

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=170)
        buf.seek(0)

        img = Image.open(buf).copy()
        buf.close()

        return img

    def make_frame_heatmap(self, points = None):
        fig = plt.figure(figsize=plt.figaspect(1))
        ax = fig.subplots()

        ax.pcolormesh(self.X, self.Y, self.Z, cmap='jet')
        ax.set_title(self.name)

        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        # plot the points if is not a None
        if points is not None:
            for point in points:
                ax.plot(point[0], point[1], 'o-', color='red', markersize=4, dash_capstyle="projecting",
                        antialiased=False, zorder=10)
                # print text with Z value
                ax.text(point[0], point[1], str(round(point[2], 2)), horizontalalignment='center',
                        verticalalignment='top', bbox=dict(facecolor='orange', alpha=0.4), zorder=11)

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=170)
        buf.seek(0)

        img = Image.open(buf).copy()
        buf.close()

        return img

    def make_frame_path(self, path = None):
        fig = plt.figure(figsize=plt.figaspect(1))
        ax = fig.subplots()

        points = np.array(path)  # Convert to a NumPy array if not already

        # Scatter plot for the points
        ax.scatter(points[:, 0], points[:, 1], color="blue", label="Points")

        # Draw lines between adjacent points
        for i in range(len(points) - 1):
            ax.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]], color="red", linewidth=1)
        # connect ends
        ax.plot([points[0][0], points[-1][0]], [points[0][1], points[-1][1]], color="red", linewidth=1)

        # Label the points for clarity
        for idx, (x, y) in enumerate(points):
            ax.text(x, y, f"{idx}", fontsize=12, ha="right")

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.legend()

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=170)
        buf.seek(0)

        img = Image.open(buf).copy()
        buf.close()

        return img

    def animate_heatmap(self):
        for one_data in self.data:
            if isinstance(one_data[0], (list, tuple, np.ndarray)):
                points = [[x[0], x[1], self.func(x)] for x in one_data]
            else:
                points = [[one_data[0], one_data[1], self.func(one_data)]]

            self.frames.append(self.make_frame_heatmap(points))

        for _ in range(10):
            self.frames.append(self.make_frame_heatmap(points))

        print(self.name + " is Done")

        # save final gif
        self.frames[0].save(self.path, save_all=True, append_images=self.frames[1:], duration=self.duration, loop=0)

        # close all frames
        for frame in self.frames:
            frame.close()


    def animate_path(self):
        for one_data in self.data:
            self.frames.append(self.make_frame_path(one_data))

        for _ in range(30):
            self.frames.append(self.make_frame_path(one_data))

        print(self.name + " is Done")

        # save final gif
        self.frames[0].save(self.path, save_all=True, append_images=self.frames[1:], duration=self.duration, loop=0)

        # close all frames
        for frame in self.frames:
            frame.close()


    def animate_3d(self):
        len_data = len(self.data)
        last_frame = None
        i = 0

        rots = int(360/self.rotation_deg_per_frame)

        # creates the animation with 360/degree_per_frame frames
        for n in range(0, rots):
            len_frames = len(self.frames)
            one_data = self.data[i]

            # update the point to be equally spread in whole animation
            if i * int(ceil((rots * .8) / len_data)) < len_frames and i + 1 < len_data:
                if isinstance(one_data[0], (list, tuple, np.ndarray)):
                    last_frame = [[x[0], x[1], self.func(x)] for x in one_data]
                else:
                    last_frame = [[one_data[0], one_data[1], self.func(one_data)]]
                i += 1

            self.frames.append(self.make_frame_3d(last_frame))
            self.add_angle += self.rotation_deg_per_frame

            # each 30 frames print % done
            if n % 30 == 0:
                print(self.name + ": " + str(n/rots * 100) + "% done")

        print(self.name + " is Done")

        # save final gif
        self.frames[0].save(self.path, save_all=True, append_images=self.frames[1:], duration=self.duration, loop=0)

        # close all frames
        for frame in self.frames:
            frame.close()
