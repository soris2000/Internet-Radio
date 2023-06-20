import flet as ft
#m3u-radio-music-playlists
#https://github.com/junguler/m3u-radio-music-playlists/blob/main/internet-radio/90s.m3u
index =0
volume = 0.5
playlist = [
    "http://198.178.121.76:8265/stream",
    "http://79.143.187.96:8000/rmin.mp3",
    "http://151.80.6.109:8090/radio.mp3",
    "http://us5.internet-radio.com:8121/stream",
    "http://stream2.dgnet.be:8008/",
    
]

def main(page:ft.Page):
    page.title = "Internet Radio"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.window_height = 500
    page.window_width = 500
    page.window_min_width = 500
    page.window_min_height = 500


# ************************      Functions          ******************************
    def on_volume_change(e: ft.PieChartEvent):
        global index
        global volume
        for idx, section in enumerate(volume_display.sections):
            if idx == e.section_index:
                section.color=ft.colors.BLUE
                section.badge.scale=0.5
                section.badge.bgcolor=ft.colors.BLUE
                v = section.badge.content.value
                page.overlay[index].volume = 0.01 * float(v)
                volume = 0.01 * float(v)
                page.update()
            else:
                section.color=ft.colors.WHITE10
                section.badge.scale=0.05
                section.badge.bgcolor=ft.colors.WHITE10
                page.overlay[index].volume =volume
        volume_display.update()

    def on_reset(e):
        global index
        global volume 
        page.overlay[index].release()
        page.overlay[index].update()
        index=0
        volume=0.5
        page.overlay[index].play()
        page.overlay[index].volume = volume
        page.update()

    def on_scan(e):
        global index
        global volume
        page.overlay[index].release()
        page.overlay[index].update()
        index = index + 1
        if index == len(page.overlay):
            index = 0
        page.overlay[index].play()
        page.overlay[index].volume = volume
        page.update()

    def on_lights(e):
        if lights.visible:
            lights.visible=False
        else:
            lights.visible=True
        page.update()
        
# *****************   Initializing player music values  **************
    # Load playlist radio to Page overlay
    for i in range(0, len(playlist)):
        station = ft.Audio(
            src=f"{playlist[i]}",
            autoplay=False,
            volume=0.5,
            balance=0,
        )
        page.overlay.append(station)

    background_image=ft.Image(
                src=f"assets/radio_bg.png",
                width=400,
                height=400,
                fit=ft.ImageFit.CONTAIN,
            )
    lights=ft.Container(width=20, height=40, bgcolor=ft.colors.AMBER_200, border_radius=50,left=190,visible=False)
                    
    icono=ft.Image(
                src=f"assets/radio_icon.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                left=150,
                        top=250,
            )
    
    btn_reset=ft.IconButton(icon=ft.icons.CIRCLE_OUTLINED,
                    icon_color=ft.colors.WHITE24,
                    icon_size=40,
                    left=105,
                    top=110,
                    on_click=on_reset)
    
    btn_scan=ft.IconButton(icon=ft.icons.CIRCLE_OUTLINED,
                     icon_color=ft.colors.WHITE24,
                    icon_size=40,
                    left=240,
                    top=110,
                    on_click=on_scan)
    
    
    btn_lights=ft.ElevatedButton(
                             width=100,
                             left=150,
                         top=190,
                         bgcolor=ft.colors.WHITE24,
                         on_click=on_lights)
    
    
    volume_display = ft.PieChart(
        sections=[
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(0),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(5),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(10),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(15),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(20),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(25),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(30),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(35),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(40),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(45),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(50),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(55),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(60),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(65),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(70),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(75),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(80),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(85),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(90),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(95),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            ft.PieChartSection(
                5,
                badge=ft.CircleAvatar(content=ft.Text(100),bgcolor=ft.colors.WHITE10,scale=0.05),
                badge_position=0.98,
                color=ft.colors.WHITE10,    
            ),
            
            
        ],
        sections_space=0,
        on_chart_event=on_volume_change,
        expand=True,
        width=80,
        height=80,
        top=58,
        left=155,
    )
    
    
    page.add(
        ft.Container(
            ft.Stack(
                [   background_image,
                    lights,
                    icono,
                    btn_reset,
                    btn_scan,
                    btn_lights,
                    volume_display,
                ]
            ),
            border_radius=8,
            width=400,
            height=400,
            
        )
    )





if __name__=="__main__":
    ft.app(target=main)
