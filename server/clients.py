# TsuserverDR, a Danganronpa Online server based on tsuserver3, an Attorney Online server
#
# Copyright (C) 2016 argoneus <argoneuscze@gmail.com> (original tsuserver3)
# Current project leader: 2018-20 Chrezm/Iuvee <thechrezm@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from enum import Enum

from server.constants import ArgType


class DefaultAO2Protocol(Enum):
    CC_INBOUND = [
        ('client_id', ArgType.INT),
        ('char_id', ArgType.INT),
        ('hdid', ArgType.STR),
        ]

    PV_OUTBOUND = [
        ('client_id', 0),  # 0
        ('char_id_tag', 'CID'),  # 1
        ('char_id', -1),  # 2
        ]

    RT_INBOUND = [
        ('name', ArgType.STR),  # 0
        ]

    RT_OUTBOUND = [
        ('name', ''),  # 0
        ]

    GM_OUTBOUND = [
        ('name', ''),  # 0
        ]

    TOD_OUTBOUND = [
        ('name', ''),  # 0
        ]


class ClientDRO1d0d0(Enum):
    MS_INBOUND = [
        ('msg_type', ArgType.STR),  # 0
        ('pre', ArgType.STR_OR_EMPTY),  # 1
        ('folder', ArgType.STR),  # 2
        ('anim', ArgType.STR),  # 3
        ('text', ArgType.STR),  # 4
        ('pos', ArgType.STR),  # 5
        ('sfx', ArgType.STR),  # 6
        ('anim_type', ArgType.INT),  # 7
        ('char_id', ArgType.INT),  # 8
        ('sfx_delay', ArgType.INT),  # 9
        ('button', ArgType.INT),  # 10
        ('evidence', ArgType.INT),  # 11
        ('flip', ArgType.INT),  # 12
        ('ding', ArgType.INT),  # 13
        ('color', ArgType.INT),  # 14
        ]

    MS_OUTBOUND = [
        ('msg_type', 0),  # 0
        ('pre', '-'),  # 1
        ('folder', '<NOCHAR>'),  # 2
        ('anim', '../../misc/blank'),  # 3
        ('msg', ''),  # 4
        ('pos', 'jud'),  # 5
        ('sfx', 0),  # 6
        ('anim_type', 0),  # 7
        ('char_id', -1),  # 8
        ('sfx_delay', 0),  # 9
        ('button', 0),  # 10
        ('evidence', 0),  # 11
        ('flip', 0),  # 12
        ('ding', -1),  # 13
        ('color', 0),  # 14
        ('showname', ' '),  # 15
        ]

    MC_INBOUND = [
        ('name', ArgType.STR),  # 0
        ('char_id', ArgType.INT),  # 1
        ]

    MC_OUTBOUND = [
        ('name', ''),  # 0
        ('char_id', -1),  # 1
        ('showname', ''),  # 2
        ]

    BN_OUTBOUND = [
        ('name', ''),  # 0
        ]


class ClientDROLegacy(Enum):
    MS_INBOUND = [
        ('msg_type', ArgType.STR),  # 0
        ('pre', ArgType.STR_OR_EMPTY),  # 1
        ('folder', ArgType.STR),  # 2
        ('anim', ArgType.STR),  # 3
        ('text', ArgType.STR),  # 4
        ('pos', ArgType.STR),  # 5
        ('sfx', ArgType.STR),  # 6
        ('anim_type', ArgType.INT),  # 7
        ('char_id', ArgType.INT),  # 8
        ('sfx_delay', ArgType.INT),  # 9
        ('button', ArgType.INT),  # 10
        ('evidence', ArgType.INT),  # 11
        ('flip', ArgType.INT),  # 12
        ('ding', ArgType.INT),  # 13
        ('color', ArgType.INT),  # 14
        ]

    MS_OUTBOUND = [
        ('msg_type', 0),  # 0
        ('pre', '-'),  # 1
        ('folder', '<NOCHAR>'),  # 2
        ('anim', '../../misc/blank'),  # 3
        ('msg', ''),  # 4
        ('pos', 'jud'),  # 5
        ('sfx', 0),  # 6
        ('anim_type', 0),  # 7
        ('char_id', 0),  # 8
        ('sfx_delay', 0),  # 9
        ('button', 0),  # 10
        ('evidence', 0),  # 11
        ('flip', 0),  # 12
        ('ding', -1),  # 13
        ('color', 0),  # 14
        ('showname', ' '),  # 15
        ]

    MC_INBOUND = [
        ('name', ArgType.STR),  # 0
        ('char_id', ArgType.INT),  # 1
        ]

    MC_OUTBOUND = [
        ('name', ''),  # 0
        ('char_id', -1),  # 1
        ]

    BN_OUTBOUND = [
        ('name', ''),  # 0
        ]


class ClientAO2d6(Enum):
    MS_INBOUND = [
        ('msg_type', ArgType.STR),  # 0
        ('pre', ArgType.STR_OR_EMPTY),  # 1
        ('folder', ArgType.STR),  # 2
        ('anim', ArgType.STR),  # 3
        ('text', ArgType.STR),  # 4
        ('pos', ArgType.STR),  # 5
        ('sfx', ArgType.STR),  # 6
        ('anim_type', ArgType.INT),  # 7
        ('char_id', ArgType.INT),  # 8
        ('sfx_delay', ArgType.INT),  # 9
        ('button', ArgType.INT),  # 10
        ('evidence', ArgType.INT),  # 11
        ('flip', ArgType.INT),  # 12
        ('ding', ArgType.INT),  # 13
        ('color', ArgType.INT),  # 14
        ('showname', ArgType.STR_OR_EMPTY),  # 15
        ('charid_pair', ArgType.INT),  # 16
        ('offset_pair', ArgType.INT),  # 17
        ('nonint_pre', ArgType.INT),  # 18
        ]

    MS_OUTBOUND = [
        ('msg_type', 0),  # 0
        ('pre', '-'),  # 1
        ('folder', '<NOCHAR>'),  # 2
        ('anim', '../../misc/blank'),  # 3
        ('msg', ''),  # 4
        ('pos', 'jud'),  # 5
        ('sfx', 0),  # 6
        ('anim_type', 0),  # 7
        ('char_id', 0),  # 8
        ('sfx_delay', 0),  # 9
        ('button', 0),  # 10
        ('evidence', 0),  # 11
        ('flip', 0),  # 12
        ('ding', -1),  # 13
        ('color', 0),  # 14
        ('showname', ' '),  # 15
        ('charid_pair', -1),  # 16
        ('other_folder', ''),  # 17
        ('other_emote', ''),  # 18
        ('offset_pair', 0),  # 19
        ('other_offset', 0),  # 20
        ('other_flip', 0),  # 21
        ('nonint_pre', 0),  # 22
        ]

    MC_INBOUND = [
        ('name', ArgType.STR),  # 0
        ('char_id', ArgType.INT),  # 1
        ('showname', ArgType.STR_OR_EMPTY),  # 2
        ]

    MC_OUTBOUND = [
        ('name', ''),  # 0
        ('char_id', -1),  # 1
        ('showname', ''),  # 2
        ]

    BN_OUTBOUND = [
        ('name', ''),  # 0
        ]


class ClientAO2d7(Enum):
    MS_INBOUND = [
        ('msg_type', ArgType.STR),  # 0
        ('pre', ArgType.STR_OR_EMPTY),  # 1
        ('folder', ArgType.STR),  # 2
        ('anim', ArgType.STR),  # 3
        ('text', ArgType.STR),  # 4
        ('pos', ArgType.STR),  # 5
        ('sfx', ArgType.STR),  # 6
        ('anim_type', ArgType.INT),  # 7
        ('char_id', ArgType.INT),  # 8
        ('sfx_delay', ArgType.INT),  # 9
        ('button', ArgType.INT),  # 10
        ('evidence', ArgType.INT),  # 11
        ('flip', ArgType.INT),  # 12
        ('ding', ArgType.INT),  # 13
        ('color', ArgType.INT),  # 14
        ('showname', ArgType.STR_OR_EMPTY),  # 15
        ('charid_pair', ArgType.INT),  # 16
        ('offset_pair', ArgType.INT),  # 17
        ('nonint_pre', ArgType.INT),  # 18
        ('looping_sfx', ArgType.INT),  # 19
        ('screenshake', ArgType.INT),  # 20
        ('frame_screenshake', ArgType.STR_OR_EMPTY),  # 21
        ('frame_realization', ArgType.STR_OR_EMPTY),  # 22
        ('frame_sfx', ArgType.STR_OR_EMPTY),  # 23
        ]

    MS_OUTBOUND = [
        ('msg_type', 0),  # 0
        ('pre', '-'),  # 1
        ('folder', '<NOCHAR>'),  # 2
        ('anim', '../../misc/blank'),  # 3
        ('msg', ''),  # 4
        ('pos', 'jud'),  # 5
        ('sfx', 0),  # 6
        ('anim_type', 0),  # 7
        ('char_id', 0),  # 8
        ('sfx_delay', 0),  # 9
        ('button', 0),  # 10
        ('evidence', 0),  # 11
        ('flip', 0),  # 12
        ('ding', -1),  # 13
        ('color', 0),  # 14
        ('showname', ' '),  # 15
        ('charid_pair', -1),  # 16
        ('other_folder', ''),  # 17
        ('other_emote', ''),  # 18
        ('offset_pair', 0),  # 19
        ('other_offset', 0),  # 20
        ('other_flip', 0),  # 21
        ('nonint_pre', 0),  # 22
        ('looping_sfx', 0),  # 23
        ('screenshake', 0),  # 24
        ('frame_screenshake', ''),  # 25
        ('frame_realization', ''),  # 26
        ('frame_sfx', ''),  # 27
        ]

    MC_INBOUND = [
        ('name', ArgType.STR),  # 0
        ('char_id', ArgType.INT),  # 1
        ('showname', ArgType.STR_OR_EMPTY),  # 2
        ]

    MC_OUTBOUND = [
        ('name', ''),  # 0
        ('char_id', -1),  # 1
        ('showname', ''),  # 2
        ]

    BN_OUTBOUND = [
        ('name', ''),  # 0
        ]


class ClientAO2d8d4(Enum):
    MS_INBOUND = [
        ('msg_type', ArgType.STR),  # 0
        ('pre', ArgType.STR_OR_EMPTY),  # 1
        ('folder', ArgType.STR),  # 2
        ('anim', ArgType.STR),  # 3
        ('text', ArgType.STR),  # 4
        ('pos', ArgType.STR),  # 5
        ('sfx', ArgType.STR),  # 6
        ('anim_type', ArgType.INT),  # 7
        ('char_id', ArgType.INT),  # 8
        ('sfx_delay', ArgType.INT),  # 9
        ('button', ArgType.INT),  # 10
        ('evidence', ArgType.INT),  # 11
        ('flip', ArgType.INT),  # 12
        ('ding', ArgType.INT),  # 13
        ('color', ArgType.INT),  # 14
        ('showname', ArgType.STR_OR_EMPTY),  # 15
        ('charid_pair_pair_order', ArgType.STR),  # 16
        ('offset_pair', ArgType.INT),  # 17
        ('nonint_pre', ArgType.INT),  # 18
        ('looping_sfx', ArgType.INT),  # 19
        ('screenshake', ArgType.INT),  # 20
        ('frame_screenshake', ArgType.STR_OR_EMPTY),  # 21
        ('frame_realization', ArgType.STR_OR_EMPTY),  # 22
        ('frame_sfx', ArgType.STR_OR_EMPTY),  # 23
        ('additive', ArgType.INT),  # 24
        ('effect', ArgType.STR),  # 25
        ]

    MS_OUTBOUND = [
        ('msg_type', 0),  # 0
        ('pre', '-'),  # 1
        ('folder', '<NOCHAR>'),  # 2
        ('anim', '../../misc/blank'),  # 3
        ('msg', ''),  # 4
        ('pos', 'jud'),  # 5
        ('sfx', 0),  # 6
        ('anim_type', 0),  # 7
        ('char_id', 0),  # 8
        ('sfx_delay', 0),  # 9
        ('button', 0),  # 10
        ('evidence', 0),  # 11
        ('flip', 0),  # 12
        ('ding', -1),  # 13
        ('color', 0),  # 14
        ('showname', ' '),  # 15
        ('charid_pair_pair_order', -1),  # 16
        ('other_folder', ''),  # 17
        ('other_emote', ''),  # 18
        ('offset_pair', 0),  # 19
        ('other_offset', 0),  # 20
        ('other_flip', 0),  # 21
        ('nonint_pre', 0),  # 22
        ('looping_sfx', 0),  # 23
        ('screenshake', 0),  # 24
        ('frame_screenshake', ''),  # 25
        ('frame_realization', ''),  # 26
        ('frame_sfx', ''),  # 27
        ('additive', 0),  # 28
        ('effect', ''),  # 29
        ]

    MC_INBOUND = [
        ('name', ArgType.STR),  # 0
        ('char_id', ArgType.INT),  # 1
        ('showname', ArgType.STR_OR_EMPTY),  # 2
        ('effects', ArgType.INT),  # 3
        ]

    MC_OUTBOUND = [
        ('name', ''),  # 0
        ('char_id', -1),  # 1
        ('showname', ''),  # 2
        ('loop', -1),  # 3
        ('channel', 0),  # 4
        ('effects', 0),  # 5
        ]

    BN_OUTBOUND = [
        ('name', ''),  # 0
        ('pos', ''),  # 1
        ]


ClientKFO2d8 = Enum('ClientKFO2d8', [(m.name, m.value) for m in ClientAO2d7])
ClientCC22 = Enum('ClientCC22', [(m.name, m.value) for m in ClientAO2d6])
ClientCC24 = Enum('ClientCC24', [(m.name, m.value) for m in ClientAO2d8d4])
