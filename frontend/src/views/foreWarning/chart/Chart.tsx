import React, { useRef, useEffect, useMemo } from "react";
import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";
import { chartStore } from "../../../store/charts";
import { useSnapshot } from "valtio";
import useWebSocketHandler from "../../../hooks/useWebSocketHandler";

const WaveformChart: React.FC = () => {
  const waveformRef = useRef<HTMLDivElement>(null);
  const chartSnapshot = useSnapshot(chartStore);
  const { readyState, connect, disconnect } = useWebSocketHandler();

  const data = useMemo(
    () => chartSnapshot.chartData.map((point) => ({ ...point })),
    [chartSnapshot.chartData]
  );

  const chartOptions = useMemo(
    () => ({
      chart: {
        type: "line",
        height: "550px",
      },
      title: {
        text: null,
      },
      xAxis: {
        title: {
          text: "ID",
        },
        gridLineWidth: 1,
        gridLineColor: "#f0f0f0",
      },
      yAxis: {
        title: {
          text: "风险分数",
        },
        gridLineWidth: 1,
        gridLineColor: "#f0f0f0",
      },
      series: [
        {
          name: "Risk Score",
          data: data,
        },
      ],
    }),
    [data]
  );

  useEffect(() => {
    if (waveformRef.current) {
      Highcharts.charts.forEach((chart) => {
        if (chart) {
          chart.series[0].setData(data, true);
        }
      });
    }
  }, [data]);

  return (
    <div className="relative w-full h-full">
      <button
        onClick={() => {
          connect();
        }}
        disabled={readyState === 1}
      >
        run
      </button>
      <button onClick={() => disconnect()}>stop</button>
      <div ref={waveformRef} className="h-full mt-6">
        <HighchartsReact highcharts={Highcharts} options={chartOptions} />
      </div>
    </div>
  );
};

export default WaveformChart;
