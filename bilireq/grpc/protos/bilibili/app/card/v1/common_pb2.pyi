"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.app.card.v1.ad_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Base(google.protobuf.message.Message):
    """条目基本信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CARD_TYPE_FIELD_NUMBER: builtins.int
    CARD_GOTO_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    THREE_POINT_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    IDX_FIELD_NUMBER: builtins.int
    AD_INFO_FIELD_NUMBER: builtins.int
    MASK_FIELD_NUMBER: builtins.int
    FROM_TYPE_FIELD_NUMBER: builtins.int
    THREE_POINT_V2_FIELD_NUMBER: builtins.int
    THREE_POINT_V3_FIELD_NUMBER: builtins.int
    DESC_BUTTON_FIELD_NUMBER: builtins.int
    THREE_POINT_V4_FIELD_NUMBER: builtins.int
    card_type: typing.Text
    """卡片类型"""

    card_goto: typing.Text
    """卡片跳转类型?"""

    goto: typing.Text
    """跳转类型
    av:视频稿件 mid:用户空间
    """

    param: typing.Text
    """目标参数"""

    cover: typing.Text
    """封面url"""

    title: typing.Text
    """标题"""

    uri: typing.Text
    """跳转uri"""

    @property
    def three_point(self) -> global___ThreePoint:
        """"""
        pass
    @property
    def args(self) -> global___Args:
        """"""
        pass
    @property
    def player_args(self) -> global___PlayerArgs:
        """"""
        pass
    idx: builtins.int
    """条目排位序号"""

    @property
    def ad_info(self) -> bilibili.app.card.v1.ad_pb2.AdInfo:
        """"""
        pass
    @property
    def mask(self) -> global___Mask:
        """"""
        pass
    from_type: typing.Text
    """来源标识
    recommend:推荐 operation:管理?
    """

    @property
    def three_point_v2(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThreePointV2]:
        """"""
        pass
    @property
    def three_point_v3(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThreePointV3]:
        """"""
        pass
    @property
    def desc_button(self) -> global___Button:
        """"""
        pass
    @property
    def three_point_v4(self) -> global___ThreePointV4:
        """三点v4"""
        pass
    def __init__(self,
        *,
        card_type: typing.Text = ...,
        card_goto: typing.Text = ...,
        goto: typing.Text = ...,
        param: typing.Text = ...,
        cover: typing.Text = ...,
        title: typing.Text = ...,
        uri: typing.Text = ...,
        three_point: typing.Optional[global___ThreePoint] = ...,
        args: typing.Optional[global___Args] = ...,
        player_args: typing.Optional[global___PlayerArgs] = ...,
        idx: builtins.int = ...,
        ad_info: typing.Optional[bilibili.app.card.v1.ad_pb2.AdInfo] = ...,
        mask: typing.Optional[global___Mask] = ...,
        from_type: typing.Text = ...,
        three_point_v2: typing.Optional[typing.Iterable[global___ThreePointV2]] = ...,
        three_point_v3: typing.Optional[typing.Iterable[global___ThreePointV3]] = ...,
        desc_button: typing.Optional[global___Button] = ...,
        three_point_v4: typing.Optional[global___ThreePointV4] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ad_info",b"ad_info","args",b"args","desc_button",b"desc_button","mask",b"mask","player_args",b"player_args","three_point",b"three_point","three_point_v4",b"three_point_v4"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ad_info",b"ad_info","args",b"args","card_goto",b"card_goto","card_type",b"card_type","cover",b"cover","desc_button",b"desc_button","from_type",b"from_type","goto",b"goto","idx",b"idx","mask",b"mask","param",b"param","player_args",b"player_args","three_point",b"three_point","three_point_v2",b"three_point_v2","three_point_v3",b"three_point_v3","three_point_v4",b"three_point_v4","title",b"title","uri",b"uri"]) -> None: ...
global___Base = Base

class Button(google.protobuf.message.Message):
    """按钮信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TEXT_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    EVENT_V2_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    text: typing.Text
    """文案"""

    param: typing.Text
    """参数"""

    uri: typing.Text
    """"""

    event: typing.Text
    """事件"""

    selected: builtins.int
    """"""

    type: builtins.int
    """类型"""

    event_v2: typing.Text
    """事件v2"""

    @property
    def relation(self) -> global___Relation:
        """关系信息"""
        pass
    def __init__(self,
        *,
        text: typing.Text = ...,
        param: typing.Text = ...,
        uri: typing.Text = ...,
        event: typing.Text = ...,
        selected: builtins.int = ...,
        type: builtins.int = ...,
        event_v2: typing.Text = ...,
        relation: typing.Optional[global___Relation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relation",b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["event",b"event","event_v2",b"event_v2","param",b"param","relation",b"relation","selected",b"selected","text",b"text","type",b"type","uri",b"uri"]) -> None: ...
global___Button = Button

class ThreePoint(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISLIKE_REASONS_FIELD_NUMBER: builtins.int
    FEEDBACKS_FIELD_NUMBER: builtins.int
    WATCH_LATER_FIELD_NUMBER: builtins.int
    @property
    def dislike_reasons(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DislikeReason]:
        """"""
        pass
    @property
    def feedbacks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DislikeReason]:
        """"""
        pass
    watch_later: builtins.int
    """稍后再看"""

    def __init__(self,
        *,
        dislike_reasons: typing.Optional[typing.Iterable[global___DislikeReason]] = ...,
        feedbacks: typing.Optional[typing.Iterable[global___DislikeReason]] = ...,
        watch_later: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dislike_reasons",b"dislike_reasons","feedbacks",b"feedbacks","watch_later",b"watch_later"]) -> None: ...
global___ThreePoint = ThreePoint

class DislikeReason(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    id: builtins.int
    """"""

    name: typing.Text
    """"""

    def __init__(self,
        *,
        id: builtins.int = ...,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","name",b"name"]) -> None: ...
global___DislikeReason = DislikeReason

class Args(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    UP_ID_FIELD_NUMBER: builtins.int
    UP_NAME_FIELD_NUMBER: builtins.int
    RID_FIELD_NUMBER: builtins.int
    RNAME_FIELD_NUMBER: builtins.int
    TID_FIELD_NUMBER: builtins.int
    TNAME_FIELD_NUMBER: builtins.int
    TRACK_ID_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    CONVERGE_TYPE_FIELD_NUMBER: builtins.int
    AID_FIELD_NUMBER: builtins.int
    type: builtins.int
    """"""

    up_id: builtins.int
    """"""

    up_name: typing.Text
    """"""

    rid: builtins.int
    """"""

    rname: typing.Text
    """"""

    tid: builtins.int
    """"""

    tname: typing.Text
    """"""

    track_id: typing.Text
    """"""

    state: typing.Text
    """"""

    converge_type: builtins.int
    """"""

    aid: builtins.int
    """"""

    def __init__(self,
        *,
        type: builtins.int = ...,
        up_id: builtins.int = ...,
        up_name: typing.Text = ...,
        rid: builtins.int = ...,
        rname: typing.Text = ...,
        tid: builtins.int = ...,
        tname: typing.Text = ...,
        track_id: typing.Text = ...,
        state: typing.Text = ...,
        converge_type: builtins.int = ...,
        aid: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aid",b"aid","converge_type",b"converge_type","rid",b"rid","rname",b"rname","state",b"state","tid",b"tid","tname",b"tname","track_id",b"track_id","type",b"type","up_id",b"up_id","up_name",b"up_name"]) -> None: ...
global___Args = Args

class PlayerArgs(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_LIVE_FIELD_NUMBER: builtins.int
    AID_FIELD_NUMBER: builtins.int
    CID_FIELD_NUMBER: builtins.int
    SUB_TYPE_FIELD_NUMBER: builtins.int
    ROOM_ID_FIELD_NUMBER: builtins.int
    EP_ID_FIELD_NUMBER: builtins.int
    IS_PREVIEW_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    SEASON_ID_FIELD_NUMBER: builtins.int
    is_live: builtins.int
    """"""

    aid: builtins.int
    """"""

    cid: builtins.int
    """"""

    sub_type: builtins.int
    """"""

    room_id: builtins.int
    """"""

    ep_id: builtins.int
    """"""

    is_preview: builtins.int
    """"""

    type: typing.Text
    """"""

    duration: builtins.int
    """"""

    season_id: builtins.int
    """"""

    def __init__(self,
        *,
        is_live: builtins.int = ...,
        aid: builtins.int = ...,
        cid: builtins.int = ...,
        sub_type: builtins.int = ...,
        room_id: builtins.int = ...,
        ep_id: builtins.int = ...,
        is_preview: builtins.int = ...,
        type: typing.Text = ...,
        duration: builtins.int = ...,
        season_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aid",b"aid","cid",b"cid","duration",b"duration","ep_id",b"ep_id","is_live",b"is_live","is_preview",b"is_preview","room_id",b"room_id","season_id",b"season_id","sub_type",b"sub_type","type",b"type"]) -> None: ...
global___PlayerArgs = PlayerArgs

class Mask(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    AVATAR_FIELD_NUMBER: builtins.int
    BUTTON_FIELD_NUMBER: builtins.int
    @property
    def avatar(self) -> global___Avatar:
        """"""
        pass
    @property
    def button(self) -> global___Button:
        """"""
        pass
    def __init__(self,
        *,
        avatar: typing.Optional[global___Avatar] = ...,
        button: typing.Optional[global___Button] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["avatar",b"avatar","button",b"button"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["avatar",b"avatar","button",b"button"]) -> None: ...
global___Mask = Mask

class Avatar(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COVER_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    EVENT_V2_FIELD_NUMBER: builtins.int
    DEFALUT_COVER_FIELD_NUMBER: builtins.int
    cover: typing.Text
    """"""

    text: typing.Text
    """"""

    uri: typing.Text
    """"""

    type: builtins.int
    """"""

    event: typing.Text
    """"""

    event_v2: typing.Text
    """"""

    defalut_cover: builtins.int
    """"""

    def __init__(self,
        *,
        cover: typing.Text = ...,
        text: typing.Text = ...,
        uri: typing.Text = ...,
        type: builtins.int = ...,
        event: typing.Text = ...,
        event_v2: typing.Text = ...,
        defalut_cover: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cover",b"cover","defalut_cover",b"defalut_cover","event",b"event","event_v2",b"event_v2","text",b"text","type",b"type","uri",b"uri"]) -> None: ...
global___Avatar = Avatar

class ThreePointV2(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TITLE_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    REASONS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    title: typing.Text
    """"""

    subtitle: typing.Text
    """"""

    @property
    def reasons(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DislikeReason]:
        """"""
        pass
    type: typing.Text
    """"""

    id: builtins.int
    """"""

    def __init__(self,
        *,
        title: typing.Text = ...,
        subtitle: typing.Text = ...,
        reasons: typing.Optional[typing.Iterable[global___DislikeReason]] = ...,
        type: typing.Text = ...,
        id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","reasons",b"reasons","subtitle",b"subtitle","title",b"title","type",b"type"]) -> None: ...
global___ThreePointV2 = ThreePointV2

class ThreePointV3(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TITLE_FIELD_NUMBER: builtins.int
    SELECTED_TITLE_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    REASONS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    SELECTED_ICON_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    DEFAULT_ID_FIELD_NUMBER: builtins.int
    title: typing.Text
    """"""

    selected_title: typing.Text
    """"""

    subtitle: typing.Text
    """"""

    @property
    def reasons(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DislikeReason]:
        """"""
        pass
    type: typing.Text
    """"""

    id: builtins.int
    """"""

    selected: builtins.int
    """"""

    icon: typing.Text
    """"""

    selected_icon: typing.Text
    """"""

    url: typing.Text
    """"""

    default_id: builtins.int
    """"""

    def __init__(self,
        *,
        title: typing.Text = ...,
        selected_title: typing.Text = ...,
        subtitle: typing.Text = ...,
        reasons: typing.Optional[typing.Iterable[global___DislikeReason]] = ...,
        type: typing.Text = ...,
        id: builtins.int = ...,
        selected: builtins.int = ...,
        icon: typing.Text = ...,
        selected_icon: typing.Text = ...,
        url: typing.Text = ...,
        default_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["default_id",b"default_id","icon",b"icon","id",b"id","reasons",b"reasons","selected",b"selected","selected_icon",b"selected_icon","selected_title",b"selected_title","subtitle",b"subtitle","title",b"title","type",b"type","url",b"url"]) -> None: ...
global___ThreePointV3 = ThreePointV3

class ThreePointV4(google.protobuf.message.Message):
    """三点v4"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SHARE_PLANE_FIELD_NUMBER: builtins.int
    WATCH_LATER_FIELD_NUMBER: builtins.int
    @property
    def share_plane(self) -> global___SharePlane:
        """分享面板信息"""
        pass
    @property
    def watch_later(self) -> global___WatchLater:
        """稍后再看"""
        pass
    def __init__(self,
        *,
        share_plane: typing.Optional[global___SharePlane] = ...,
        watch_later: typing.Optional[global___WatchLater] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["share_plane",b"share_plane","watch_later",b"watch_later"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["share_plane",b"share_plane","watch_later",b"watch_later"]) -> None: ...
global___ThreePointV4 = ThreePointV4

class SharePlane(google.protobuf.message.Message):
    """分享面板信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ShareToEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: builtins.bool
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: builtins.bool = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    TITLE_FIELD_NUMBER: builtins.int
    SHARE_SUBTITLE_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    AID_FIELD_NUMBER: builtins.int
    BVID_FIELD_NUMBER: builtins.int
    SHARE_TO_FIELD_NUMBER: builtins.int
    AUTHOR_FIELD_NUMBER: builtins.int
    AUTHOR_ID_FIELD_NUMBER: builtins.int
    SHORT_LINK_FIELD_NUMBER: builtins.int
    PLAY_NUMBER_FIELD_NUMBER: builtins.int
    title: typing.Text
    """标题"""

    share_subtitle: typing.Text
    """副标贴文案"""

    desc: typing.Text
    """备注"""

    cover: typing.Text
    """封面url"""

    aid: builtins.int
    """稿件avid"""

    bvid: typing.Text
    """稿件bvid"""

    @property
    def share_to(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.bool]:
        """允许分享方式"""
        pass
    author: typing.Text
    """UP主昵称"""

    author_id: builtins.int
    """UP主mid"""

    short_link: typing.Text
    """短连接"""

    play_number: typing.Text
    """播放次数文案"""

    def __init__(self,
        *,
        title: typing.Text = ...,
        share_subtitle: typing.Text = ...,
        desc: typing.Text = ...,
        cover: typing.Text = ...,
        aid: builtins.int = ...,
        bvid: typing.Text = ...,
        share_to: typing.Optional[typing.Mapping[typing.Text, builtins.bool]] = ...,
        author: typing.Text = ...,
        author_id: builtins.int = ...,
        short_link: typing.Text = ...,
        play_number: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aid",b"aid","author",b"author","author_id",b"author_id","bvid",b"bvid","cover",b"cover","desc",b"desc","play_number",b"play_number","share_subtitle",b"share_subtitle","share_to",b"share_to","short_link",b"short_link","title",b"title"]) -> None: ...
global___SharePlane = SharePlane

class WatchLater(google.protobuf.message.Message):
    """稍后再看信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    AID_FIELD_NUMBER: builtins.int
    BVID_FIELD_NUMBER: builtins.int
    aid: builtins.int
    """稿件avid"""

    bvid: typing.Text
    """稿件bvid"""

    def __init__(self,
        *,
        aid: builtins.int = ...,
        bvid: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aid",b"aid","bvid",b"bvid"]) -> None: ...
global___WatchLater = WatchLater

class ReasonStyle(google.protobuf.message.Message):
    """标签框信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TEXT_FIELD_NUMBER: builtins.int
    TEXT_COLOR_FIELD_NUMBER: builtins.int
    BG_COLOR_FIELD_NUMBER: builtins.int
    BORDER_COLOR_FIELD_NUMBER: builtins.int
    ICON_URL_FIELD_NUMBER: builtins.int
    TEXT_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    BG_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    BORDER_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    ICON_NIGHT_URL_FIELD_NUMBER: builtins.int
    BG_STYLE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    ICON_BG_URL_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    EVENT_V2_FIELD_NUMBER: builtins.int
    RIGHT_ICON_TYPE_FIELD_NUMBER: builtins.int
    LEFT_ICON_TYPE_FIELD_NUMBER: builtins.int
    text: typing.Text
    """文案"""

    text_color: typing.Text
    """文字颜色"""

    bg_color: typing.Text
    """背景色"""

    border_color: typing.Text
    """边框色"""

    icon_url: typing.Text
    """图标url"""

    text_color_night: typing.Text
    """文字颜色-夜间"""

    bg_color_night: typing.Text
    """背景色-夜间"""

    border_color_night: typing.Text
    """边框色-夜间"""

    icon_night_url: typing.Text
    """图标url-夜间"""

    bg_style: builtins.int
    """背景风格id
    1:无背景 2:有背景
    """

    uri: typing.Text
    """"""

    icon_bg_url: typing.Text
    """"""

    event: typing.Text
    """"""

    event_v2: typing.Text
    """"""

    right_icon_type: builtins.int
    """"""

    left_icon_type: typing.Text
    """"""

    def __init__(self,
        *,
        text: typing.Text = ...,
        text_color: typing.Text = ...,
        bg_color: typing.Text = ...,
        border_color: typing.Text = ...,
        icon_url: typing.Text = ...,
        text_color_night: typing.Text = ...,
        bg_color_night: typing.Text = ...,
        border_color_night: typing.Text = ...,
        icon_night_url: typing.Text = ...,
        bg_style: builtins.int = ...,
        uri: typing.Text = ...,
        icon_bg_url: typing.Text = ...,
        event: typing.Text = ...,
        event_v2: typing.Text = ...,
        right_icon_type: builtins.int = ...,
        left_icon_type: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bg_color",b"bg_color","bg_color_night",b"bg_color_night","bg_style",b"bg_style","border_color",b"border_color","border_color_night",b"border_color_night","event",b"event","event_v2",b"event_v2","icon_bg_url",b"icon_bg_url","icon_night_url",b"icon_night_url","icon_url",b"icon_url","left_icon_type",b"left_icon_type","right_icon_type",b"right_icon_type","text",b"text","text_color",b"text_color","text_color_night",b"text_color_night","uri",b"uri"]) -> None: ...
global___ReasonStyle = ReasonStyle

class LikeButton(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    AID_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    SHOW_COUNT_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    EVENT_V2_FIELD_NUMBER: builtins.int
    Aid: builtins.int
    """"""

    count: builtins.int
    """"""

    show_count: builtins.bool
    """"""

    event: typing.Text
    """"""

    selected: builtins.int
    """"""

    event_v2: typing.Text
    """"""

    def __init__(self,
        *,
        Aid: builtins.int = ...,
        count: builtins.int = ...,
        show_count: builtins.bool = ...,
        event: typing.Text = ...,
        selected: builtins.int = ...,
        event_v2: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["Aid",b"Aid","count",b"count","event",b"event","event_v2",b"event_v2","selected",b"selected","show_count",b"show_count"]) -> None: ...
global___LikeButton = LikeButton

class Up(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    AVATAR_FIELD_NUMBER: builtins.int
    OFFICIAL_ICON_FIELD_NUMBER: builtins.int
    DESC_BUTTON_FIELD_NUMBER: builtins.int
    COOPERATION_FIELD_NUMBER: builtins.int
    id: builtins.int
    """"""

    name: typing.Text
    """"""

    desc: typing.Text
    """"""

    @property
    def avatar(self) -> global___Avatar:
        """"""
        pass
    official_icon: builtins.int
    """"""

    @property
    def desc_button(self) -> global___Button:
        """"""
        pass
    cooperation: typing.Text
    """"""

    def __init__(self,
        *,
        id: builtins.int = ...,
        name: typing.Text = ...,
        desc: typing.Text = ...,
        avatar: typing.Optional[global___Avatar] = ...,
        official_icon: builtins.int = ...,
        desc_button: typing.Optional[global___Button] = ...,
        cooperation: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["avatar",b"avatar","desc_button",b"desc_button"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["avatar",b"avatar","cooperation",b"cooperation","desc",b"desc","desc_button",b"desc_button","id",b"id","name",b"name","official_icon",b"official_icon"]) -> None: ...
global___Up = Up

class Relation(google.protobuf.message.Message):
    """关系信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int
    IS_FOLLOW_FIELD_NUMBER: builtins.int
    IS_FOLLOWED_FIELD_NUMBER: builtins.int
    status: builtins.int
    """关系状态"""

    is_follow: builtins.int
    """是否关注"""

    is_followed: builtins.int
    """是否粉丝"""

    def __init__(self,
        *,
        status: builtins.int = ...,
        is_follow: builtins.int = ...,
        is_followed: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_follow",b"is_follow","is_followed",b"is_followed","status",b"status"]) -> None: ...
global___Relation = Relation
