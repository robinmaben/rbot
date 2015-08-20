from dashboard.models import CrawlStartPoint


class Launcher(object):
    thread_count = 0

    @staticmethod
    def launch(self):
        self.thread_count += 1
        start_points = CrawlStartPoint.objects.all()
        for start_point in start_points:
            print start_point
