import { default as Janus, JanusJS } from '../vendor/janus-gateway/janus';

class JanusService {
  protocol: string;
  hostname: string;
  port: string;
  url: URL;

  deviceId: string;
  token: string;

  janus: Janus;
  stream?: JanusJS.PluginHandle;

  initOptions: JanusJS.InitOptions;
  constructorOptions: JanusJS.ConstructorOptions;
  pluginOptions: JanusJS.PluginOptions;

  constructor(
    protocol: string, 
    hostname: string, 
    port: string,
    token: string,
    deviceId: string,
    initOptions?: JanusJS.InitOptions,
    constructorOptions?: JanusJS.ConstructorOptions,
    pluginOptions?: JanusJS.PluginOptions
  ) {
    this.protocol = protocol;
    this.hostname = hostname;
    this.port = port;
    this.url = new URL(
      `${protocol}${hostname}${port}/janus`
    );
    
    this.deviceId = deviceId;
    this.token = token;
    
    const self = this;

    if (typeof initOptions === undefined){
      initOptions = this.defaultInitOptions()
    }

    if (typeof constructorOptions === undefined){
      constructorOptions = this.defaultConstructorOptions();
    }

    if (typeof pluginOptions === undefined){
      pluginOptions = this.defaultPluginOptions();
    }

    this.initOptions = initOptions;
    this.constructorOptions = constructorOptions;
    this.pluginOptions = pluginOptions;

    Janus.init(this.initOptions);

    this.janus = new Janus(this.constructorOptions)
  }

  defaultPluginOptions(): JanusJS.PluginOptions {
    const opaqueId = `device-${this.deviceId}-${Janus.randomString(12)}`;

    return {
      plugin: "janus.plugin.streaming",
      opaqueId: opaqueId,
      success: this.onStreamReady,
      error: this.onAttachError,
      iceState: this.onIceState,
      webrtcState: this.onWebrtcState,
      mediaState: this.onMediaState,
      slowLink: this.onSlowLink,
      onmessage: this.onMessage,
      onlocalstream: this.onLocalStream,
      onremotestream: this.onRemoteStream,
      ondataopen: this.onDataChannelOpen,
      ondata: this.onDataChannelMessage,
      oncleanup: this.onCleanup,
      detached: this.onDetatched
    }
  }

  defaultConstructorOptions(): JanusJS.ConstructorOptions{
    return {
      server: this.url.toString(),
      // TODO ICE
      // iceServers: [],
      withCredentials: true,
      token: this.token,
      ipv6: false,
      destroyOnUnload: true,
      success: this.onSessionCreate,
      error: this.onSessionError,
      destroyed: this.onSessionDestroyed,
    }
  }

  defaultInitOptions(): JanusJS.InitOptions {
    return {
      callback: this.onInit,
      debug: true
    }
  }

  onStreamReady(handle: JanusJS.PluginHandle) {
    this.stream = handle
  }

  onCleanup(){
    console.info("Janus plugin cleanup");
  }

  onDetatched(){
    console.info("Janus plugin detatched");
  }

  onDataChannelMessage(){
    console.info("Data channel message received");
  }

  onDataChannelOpen(){
    console.info("Data channel opened");
  }

  onRemoteStream(stream: MediaStream){
    console.info("Remote stream started", stream);
  }

  onLocalStream(stream: MediaStream){
    console.info("Local stream started", stream);
  }

  onMessage(message: JanusJS.Message, jsep?: JanusJS.JSEP){
    console.info("Message & jsep received", message, jsep);
  }

  onSlowLink(state: { uplink: boolean }){
    console.warn("Slow link detected", state);
  }

  onMediaState(medium: 'audio' | 'video', receiving: boolean, mid?: number){
    console.info(`Media state changed medium=${medium} receiving=${receiving} mid=${mid}`);
  }

  onWebrtcState(isConnected: boolean){
    console.info("WebRTC PeerConnection connected", isConnected);
  }

  onIceState(state: 'connected' | 'failed' | 'disconnected' | 'closed'){
    console.info("Ice state changed: ", state);
  }

  onAttachError(error: any) {
    console.error("Error attaching plugin", error);
  }

  connect(){
    this.janus.attach(this.pluginOptions)
  }

  onSessionDestroyed(callback?: Function){
    console.debug("Janus.onSessionDestroyed called", callback)
    if (callback){
      console.debug("Janus.onSessionDestroyed callback", callback)
      callback();
    }
  }

  onSessionError(callback?: Function){
    console.error("Janus.onSessionError called", callback)
    if (callback){
      console.debug("Janus.onSessionError callback", callback)
      callback();
    }
  }

  onSessionCreate(callback?: Function){
    console.debug("Janus.onSessionCreateSuccess called", callback);
    this.connect();
    if (callback){
      console.debug("Janus.onSessionCreateSuccess callback", callback);
      callback();
    }
  }

  onInit(callback?: Function){
    console.debug("Janus.onInit called", callback)
    if (callback){
      console.debug("Janus.onInit callback", callback)
      callback();
    }
  }
}

export default JanusService