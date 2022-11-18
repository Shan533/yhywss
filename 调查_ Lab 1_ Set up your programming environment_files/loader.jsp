

function parentFrameUefModeOriginalUseUefSupportCenterVariable() {
    try {
        return window.parent.var_uefModeOriginalUseUefSupportCenter;
    }
    catch (e) {
        return undefined;
    }
}

/* debug userName = "sessionkey"; */

var var_key = "34146365-66d0-11ed-9c26-120f0247dc5b";
var var_dashboard_url = "https://neucanvas.eesysoft.com";
var var_loadfile = "https://neucanvas.eesysoft.com/loadFile";
var var_style_path = "https://neucanvas.eesysoft.com/resources";
var var_stamp = "20221117235024";
var var_eesy_build = "38";
var var_eesy_dbUpdateCount = "11491";
var var_eesy_userUpdated = undefined;
var var_eesy_user_walkthrough_progress_updated = undefined;
var var_eesy_style_checksum = "-1318802676";
var var_show_tab_initial = false;
var var_show_tab = var_show_tab_initial;
var var_tab_version = 2;
var var_proactive_version = 3;
var var_proactive_lms = "canvas";
var var_proactive_dark = false;
var var_open_as_chat = false;
var var_moveable_tab = true;
var var_language = -1;
var var_expert_language = -1;
var var_uefMode = false;
var var_isLtiLaunch = false;
var var_ltiEngineIsPresent = false;
var var_uefModeOriginal = !var_uefMode && (window.name === "classic-learn-iframe");
var var_uefModeOriginalUseUefSupportCenter = false;
var isUefOriginalSupportCenter = !var_uefMode && (var_uefModeOriginalUseUefSupportCenter || parentFrameUefModeOriginalUseUefSupportCenterVariable());
var var_loadExpertTool = true;
var var_isExpertToolChromePlugin = false;
var eesyTemplates;
var waitforload = false;
var supportTabMinimized = undefined;
var scrollbarRightAdjust = '19px';
var supportTabMoveLimit = '50';
var eesy_minimizedTabWidth = '8px';
var eesy_maximizedTabWidth = '';
var attemptUnobscure = false;
var doNotLoadEngineForUserAgentPattern = 'not_in_use_05231;';
var var_eesy_hiddenHelpItems = undefined;
var var_eesy_sac = undefined;
var var_eesy_helpitemsSeen = undefined;
var var_user_map = {"isDebug":false,"userUpdatedStamp":"20220924043659","expertLanguageId":-1,"supportTabPosition":null,"reset_views_stamp":"","isShowTab":false,"languageId":-1,"isSupportTabMinimized":false,"id":76838,"userWalkthroughProgressUpdatedStamp":"0"};
var var_instance_name = "neucanvas";

function eesy_load_js(jsUrl) {
  var fileref = document.createElement("script");
  fileref.setAttribute("type", "text/javascript");
  fileref.setAttribute("src", jsUrl);
  document.getElementsByTagName("head")[0].appendChild(fileref);
}

eesy_load_js(var_dashboard_url + "/loader.js?__bn=" + var_eesy_build);
