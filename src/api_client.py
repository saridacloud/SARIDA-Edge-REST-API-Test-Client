#!/usr/bin/env python3
import json

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models import FrameAnalysisDetails, AnalysisDetails, Polygon, Point

from PySide6.QtGui import QPolygon
from PySide6.QtCore import QPoint


class SaridaEdgeApiWrapper:
    def __init__(self) -> None:
        self.configuration = swagger_client.Configuration()
        self.api_client = None

    def setConfig(self, config):
        try:
            if 'SWAGGER_CONFIG' in config:
                self.configuration.host = config['SWAGGER_CONFIG']['host']
                self.configuration.temp_folder_path = config['SWAGGER_CONFIG']['temp_folder_path']
        except KeyError as e:
            print('Exception while reading config: %s\n' % e)
        self.api_client = swagger_client.ApiClient(configuration=self.configuration)

    def analysisResultsCurrentGet(self) -> bool:
        try:
            analysis_client = swagger_client.AnalysisApi(self.api_client)
            return analysis_client.analysis_results_current_get()
        except ApiException as e:
            print(
                'Exception when calling AnalysisApi->analysis_results_current_get: %s\n'
                % e
            )
        return False

    def analysisResultsDetailsCurrentGet(self) -> FrameAnalysisDetails:
        try:
            analysis_client = swagger_client.AnalysisApi(self.api_client)
            return analysis_client.analysis_results_details_current_get()
        except ApiException as e:
            print(
                'Exception when calling AnalysisApi->analysis_results_details_current_get: %s\n'
                % e
            )
        return ''

    def analysisResultsDetailsToQPolygon(
        self, call_result: FrameAnalysisDetails
    ) -> QPolygon:
        result_polygon = QPolygon()

        if not call_result.analysis_details or len(call_result.analysis_details) < 1:
            return result_polygon

        analysis_details: AnalysisDetails
        analysis_details = call_result.analysis_details[0]

        current_polygon: Polygon
        current_polygon = analysis_details.polygon

        current_point: Point
        for current_point in current_polygon.point_list:
            result_polygon.append(QPoint(current_point.x, current_point.y))

        return result_polygon


if __name__ == '__main__':
    from appsettings import loadConfig
    config = loadConfig()
    api = SaridaEdgeApiWrapper()
    api.setConfig(config)