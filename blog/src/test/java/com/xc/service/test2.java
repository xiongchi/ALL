package com.xc.service;

import com.alibaba.fastjson.*;
import com.alibaba.fastjson.serializer.JSONSerializer;
import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by xiongchi on 2017/11/7.
 */
public class test2 {

    public static void main(String[] args) {
        String str = "{\n" +
                "  \"terminalGroup\":[\n" +
                "    {\n" +
                "      \"id\":\"LMS1_A6:terminal 7\",\n" +
                "      \"alias\":\"第一号泊位(D3-D4)\",\n" +
                "      \"protocolRef\":\"Dock3-1\",\n" +
                "      \"serviceGroup\":[\n" +
                "        \"LMS1_A6:terminal 7:TerminalDistance\" ,\n" +
                "        \"LMS1_A6:terminal 7:VesselAngle\" ,\n" +
                "        \"LMS1_A6:terminal 7:TerminalSpeed\"\n" +
                "      ],\n" +
                "      \"dockingAlarmOptionsRef\":\"dockingAlarm-1\",\n" +
                "      \"mooringEdgeOptionsRef\":\"mooringEdge-1\",\n" +
                "      \"hookStation\":{\n" +
                "        \"id\":\"hookStation\",\n" +
                "        \"protocolRef\":\"Dock4\",\n" +
                "        \"hooksGroup\":[\n" +
                "          {\n" +
                "            \"id\":\"p9\",\n" +
                "            \"alias\":\"1号钩\",\n" +
                "            \"service\":\"HS1:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"Q-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P8-2\",\n" +
                "            \"alias\":\"2号钩\",\n" +
                "            \"service\":\"HS2:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"T-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P8-1\",\n" +
                "            \"alias\":\"3号钩\",\n" +
                "            \"service\":\"HS3:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"T-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "          \"id\":\"P7-2\",\n" +
                "          \"alias\":\"4号钩\",\n" +
                "          \"service\":\"HS4:HookStation:HookStationStatus\",\n" +
                "          \"type\":\"D-Hooks\",\n" +
                "          \"nameGroup\":[\n" +
                "          \"A\",\"B\",\"C\",\"D\"\n" +
                "          ],\n" +
                "          \"hooksAlarmOptions\":{\n" +
                "          \"alert\":50,\n" +
                "          \"warn\":75,\n" +
                "          \"max\":150\n" +
                "          }\n" +
                "          },\n" +
                "          {\n" +
                "          \"id\":\"P7-1\",\n" +
                "          \"alias\":\"5号钩\",\n" +
                "          \"service\":\"HS5:HookStation:HookStationStatus\",\n" +
                "          \"type\":\"D-Hooks\",\n" +
                "          \"nameGroup\":[\n" +
                "          \"A\",\"B\",\"C\",\"D\"\n" +
                "          ],\n" +
                "          \"hooksAlarmOptions\":{\n" +
                "          \"alert\":50,\n" +
                "          \"warn\":75,\n" +
                "          \"max\":150\n" +
                "          }\n" +
                "          },\n" +
                "          {\n" +
                "          \"id\":\"P6\",\n" +
                "          \"alias\":\"6号钩\",\n" +
                "          \"service\":\"HS6:HookStation:HookStationStatus\",\n" +
                "          \"type\":\"Q-Hooks\",\n" +
                "          \"nameGroup\":[\n" +
                "          \"A\",\"B\",\"C\",\"D\"\n" +
                "          ],\n" +
                "          \"hooksAlarmOptions\":{\n" +
                "          \"alert\":50,\n" +
                "          \"warn\":75,\n" +
                "          \"max\":150\n" +
                "          }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P5-2\",\n" +
                "            \"alias\":\"7号钩\",\n" +
                "            \"service\":\"HS7:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"Q-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P5-1\",\n" +
                "            \"alias\":\"8号钩\",\n" +
                "            \"service\":\"HS8:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"Q-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P4\",\n" +
                "            \"alias\":\"9号钩\",\n" +
                "            \"service\":\"HS9:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"Q-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P3-2\",\n" +
                "            \"alias\":\"10号钩\",\n" +
                "            \"service\":\"HS10:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"D-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P3-1\",\n" +
                "            \"alias\":\"11号钩\",\n" +
                "            \"service\":\"HS11:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"D-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P2-2\",\n" +
                "            \"alias\":\"12号钩\",\n" +
                "            \"service\":\"HS12:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"D-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P2-1\",\n" +
                "            \"alias\":\"13号钩\",\n" +
                "            \"service\":\"HS13:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"D-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          },\n" +
                "          {\n" +
                "            \"id\":\"P1\",\n" +
                "            \"alias\":\"14号钩\",\n" +
                "            \"service\":\"HS14:HookStation:HookStationStatus\",\n" +
                "            \"type\":\"Q-Hooks\",\n" +
                "            \"nameGroup\":[\n" +
                "              \"A\",\"B\",\"C\",\"D\"\n" +
                "            ],\n" +
                "            \"hooksAlarmOptions\":{\n" +
                "              \"alert\":50,\n" +
                "              \"warn\":75,\n" +
                "              \"max\":150\n" +
                "            }\n" +
                "          }\n" +
                "        ]\n" +
                "      },\n" +
                "      \"laser\":{\n" +
                "        \"protocolRef\":\"Dock3-1\",\n" +
                "        \"leftService\":\"LMS1_A6:LaserLeft_1:Distance\",\n" +
                "        \"rightService\":\"LMS1_A6:LaserRight_1:Distance\",\n" +
                "        \"leftTimeout\":\"LMS1_A6:LaserLeft_1:Alarm\",\n" +
                "        \"rightTimeout\":\"LMS1_A6:LaserRight_1:Alarm\"\n" +
                "      }\n" +
                "    }\n" +
                "  ],\n" +
                "  \"dockingAlarmOptionsGroup\":[\n" +
                "    {\n" +
                "      \"id\":\"dockingAlarm-1\",\n" +
                "      \"angleAlert\":8,\n" +
                "      \"angleWarn\":10,\n" +
                "      \"speedMax\":20,\n" +
                "      \"speedMin\":0,\n" +
                "      \"speedAlert\":10,\n" +
                "      \"speedWarn\":16,\n" +
                "      \"mooringMax\":2.5,\n" +
                "      \"mooringMin\":-2,\n" +
                "      \"mooringAlert\":1,\n" +
                "      \"mooringWarn\":1.5,\n" +
                "      \"extrusionAlert\":-0.5,\n" +
                "      \"extrusionWarn\":-1.2\n" +
                "    }\n" +
                "  ],\n" +
                "  \"mooringEdgeOptionsGroup\":[\n" +
                "    {\n" +
                "      \"id\":\"mooringEdge-1\",\n" +
                "      \"enterMooringDistance\":2,\n" +
                "      \"leaveMooringDistance\":2.5,\n" +
                "      \"enterMooringSpeed\":2\n" +
                "    }\n" +
                "  ],\n" +
                "  \"environmentGroup\":[\n" +
                "    {\n" +
                "      \"id\":\"A5:Wind\",\n" +
                "      \"type\":\"WIND\",\n" +
                "      \"alias\":\"第一号风力风向(D3)\",\n" +
                "      \"protocolRef\":\"Dock3-1\",\n" +
                "      \"serviceGroup\":[\n" +
                "        \"A5:Wind:WindSpeed\",\"A5:Wind:Direction\"\n" +
                "      ],\n" +
                "      \"aliasGroup\":[\n" +
                "        \"1#风力(D3)\",\"1#风向(D3)\"\n" +
                "      ]\n" +
                "    },\n" +
                "    {\n" +
                "      \"id\":\"BOX1 A3:AWAC\",\n" +
                "      \"type\":\"CURRENT\",\n" +
                "      \"alias\":\"第一号层流(C)\",\n" +
                "      \"protocolRef\":\"Coneall\",\n" +
                "      \"serviceGroup\":[\n" +
                "        \"BOX1 A3:AWAC\"\n" +
                "      ],\n" +
                "      \"aliasGroup\":[\n" +
                "        \"1#层流之单层流速(C)\",\"1#层流之单层流向(C)\",\"1#层流之多层流速(C)\",\n" +
                "        \"1#层流之多层流向(C)\",\"1#海水温度(C)\"\n" +
                "      ]\n" +
                "    },\n" +
                "    {\n" +
                "      \"id\":\"A8:HUMIDITY\",\n" +
                "      \"type\":\"HUMIDITY\",\n" +
                "      \"alias\":\"第一号湿度(C)\",\n" +
                "      \"protocolRef\":\"Coneall\",\n" +
                "      \"serviceGroup\":[\n" +
                "        \"A8:HUMIDITY\"\n" +
                "      ]\n" +
                "    },\n" +
                "    {\n" +
                "      \"id\":\"A8:TEMPERATURE\",\n" +
                "      \"type\":\"TEMPERATURE\",\n" +
                "      \"alias\":\"第一号温度(C)\",\n" +
                "      \"protocolRef\":\"Coneall\",\n" +
                "      \"serviceGroup\":[\n" +
                "        \"A8:TEMPERATURE\"\n" +
                "      ]\n" +
                "    },\n" +
                "    {\n" +
                "      \"id\":\"A9:VISIBILITY\",\n" +
                "      \"type\":\"VISIBILITY\",\n" +
                "      \"alias\":\"第二号可见度(D5)\",\n" +
                "      \"protocolRef\":\"Dock5\",\n" +
                "      \"serviceGroup\":[\n" +
                "        \"A9:VISIBILITY\"\n" +
                "      ]\n" +
                "    },\n" +
                "    {\n" +
                "      \"id\":\"A12:WAVE\",\n" +
                "      \"type\":\"WAVE\",\n" +
                "      \"alias\":\"第二号波浪(D5)\",\n" +
                "      \"protocolRef\":\"Dock5\",\n" +
                "      \"serviceGroup\":[\n" +
                "        \"A12:WAVE\"\n" +
                "      ]\n" +
                "    },\n" +
                "    {\n" +
                "      \"id\":\"A12:TIDE\",\n" +
                "      \"type\":\"TIDE\",\n" +
                "      \"alias\":\"第一号潮汐(D3)\",\n" +
                "      \"protocolRef\":\"Dock3-1\",\n" +
                "      \"serviceGroup\":[\n" +
                "        \"A12:TIDE:Tide\"\n" +
                "      ]\n" +
                "    }\n" +
                "  ],\n" +
                "  \"environmentAlarmOptionsGroup\":{\n" +
                "    \"id\":\"environmentAlarm\",\n" +
                "    \"windAlarmOptions\":{\n" +
                "      \"max\":60,\n" +
                "      \"min\":0,\n" +
                "      \"unit\":\"M/S\",\n" +
                "      \"alert\":10,\n" +
                "      \"warn\":17\n" +
                "    },\n" +
                "    \"currentAlarmOptions\":{\n" +
                "      \"currentMax\":2,\n" +
                "      \"currentMin\":0,\n" +
                "      \"currentUnit\":\"m/s\",\n" +
                "      \"currentAlert\":1,\n" +
                "      \"currentWarn\":1.5,\n" +
                "      \"waterTemperatureMax\":30,\n" +
                "      \"waterTemperatureMin\":-10,\n" +
                "      \"waterTemperatureUnit\":\"℃\",\n" +
                "      \"waterTemperatureAlert\":20,\n" +
                "      \"waterTemperatureWarn\":25\n" +
                "    },\n" +
                "    \"humidityAlarmOptions\":{\n" +
                "      \"max\":100,\n" +
                "      \"min\":0,\n" +
                "      \"unit\":\"%\",\n" +
                "      \"alert\":75,\n" +
                "      \"warn\":90\n" +
                "    },\n" +
                "    \"temperatureAlarmOptions\":{\n" +
                "      \"max\":40,\n" +
                "      \"min\":-20,\n" +
                "      \"unit\":\"℃\",\n" +
                "      \"alert\":30,\n" +
                "      \"warn\":37\n" +
                "    },\n" +
                "    \"visibilityAlarmOptions\":{\n" +
                "      \"max\":30,\n" +
                "      \"min\":0,\n" +
                "      \"unit\":\"km\",\n" +
                "      \"alert\":5,\n" +
                "      \"warn\":20\n" +
                "    },\n" +
                "    \"tideAlarmOptions\":{\n" +
                "      \"max\":10,\n" +
                "      \"min\":-5,\n" +
                "      \"unit\":\"m\",\n" +
                "      \"alert\":-1,\n" +
                "      \"warn\":2\n" +
                "    },\n" +
                "    \"waveAlarmOptions\":{\n" +
                "      \"sigWaveAlert\":1.6,\n" +
                "      \"sigWaveWarn\":1.8,\n" +
                "      \"unit\":\"m\",\n" +
                "      \"longWaveAlert\":1.2,\n" +
                "      \"longWaveWarn\":1.6\n" +
                "    }\n" +
                "  },\n" +
                "  \"protocols\":{\n" +
                "    \"coneall\":{\n" +
                "      \"id\":\"Coneall\",\n" +
                "      \"mcastPort\":8123,\n" +
                "      \"mcastHost\":\"224.0.0.3\",\n" +
                "      \"frequency\":\"6005\",\n" +
                "      \"onChange\":\"1\"\n" +
                "    },\n" +
                "    \"dock3\":[\n" +
                "      {\n" +
                "        \"id\":\"Dock3-1\",\n" +
                "        \"mcastPort\":42312,\n" +
                "        \"mcastHost\":\"224.2.2.2\",\n" +
                "        \"tcpPort\":10026,\n" +
                "        \"tcpHost\":\"192.168.1.174\"\n" +
                "      },\n" +
                "      {\n" +
                "        \"id\":\"Dock3-2\",\n" +
                "        \"mcastPort\":42313,\n" +
                "        \"mcastHost\":\"224.2.2.3\",\n" +
                "        \"tcpPort\":10027,\n" +
                "        \"tcpHost\":\"192.168.1.174\"\n" +
                "      }\n" +
                "    ],\n" +
                "    \"dock4\":{\n" +
                "      \"id\":\"Dock4\",\n" +
                "      \"mcastPort\":5001,\n" +
                "      \"mcastHost\":\"225.1.2.3\",\n" +
                "      \"frequency\":\"6005\",\n" +
                "      \"onChange\":\"1\"\n" +
                "    },\n" +
                "    \"dock5\":{\n" +
                "      \"id\":\"Dock5\",\n" +
                "      \"mcastPort\":5002,\n" +
                "      \"mcastHost\":\"225.1.2.4\",\n" +
                "      \"frequency\":\"6005\",\n" +
                "      \"onChange\":\"1\"\n" +
                "    }\n" +
                "  },\n" +
                "  \"commonOptions\":{\n" +
                "    \"noReceiveTimeout\":15000,\n" +
                "    \"pollingPeriod\":3000\n" +
                "  }\n" +
                "}";
        Gson gson = new Gson();
        Map map = gson.fromJson(str, HashMap.class);
        System.out.println(map.get("terminalGroup"));
        ArrayList arr = (ArrayList) map.get("terminalGroup");
        System.out.println(arr.get(0));
        Map m = (Map) arr.get(0);
        System.out.println(m.get("hookStation"));
//        Map jsonObject= JSON.parseObject(str,new TypeReference<Map>(){});
//        JSONArray l = (JSONArray) jsonObject.get("terminalGroup");
//        JSONObject jj = (JSONObject) l.get(0);
//        System.out.println(jj.get("hookStation"));
//        System.out.println(jj);
//        System.out.println(jj.toJSONString());
        // JSONArray arr = JSON.parseArray(jj.toJSONString());
//        System.out.println(arr.get(7));
//        List<List<Map<String, Object> >> mapList = (List) l;
//        List<Map<String, Object>> fu = (List<Map<String, Object>>) l.get(0);
//        System.out.println(fu);
       // Map ll = (Map) l.get(0);
//        System.out.println(l);
//        System.out.println(ll);
//        System.out.println(jsonObject);

    }
}
