from lxml import html
import requests
import re
import os
import urllib3

def createDir(path):
    if not os.path.exists(path): os.makedirs(path)

# Settings
iosVersion = "13.1.3"
downloadAll = [
    "SpringBoard",
    "ABMHelper",
    "ACTFramework",
    "AMPCoreUI",
    "AOPHaptics",
    "AOSKit",
    "APTransport",
    "ARDisplayDevice",
    "ARKit",
    "ASEProcessing",
    "ATFoundation",
    "AVConference",
    "AVFAudio",
    "AVFoundation",
    "AVKit",
    "AXAggregateStatisticsServices",
    "AXContainerServices",
    "AXCoreUtilities",
    "AXElementInteraction",
    "AXFrontBoardUtils",
    "AXLocalizationCaptionService",
    "AXMediaUtilities",
    "AXRuntime",
    "AXSpeakFingerManager",
    "AXSpeechAssetServices",
    "AXSpringBoardServerInstance",
    "AXTapToSpeakTime",
    "Accelerate",
    "Accessibility",
    "AccessibilityPhysicalInteraction",
    "AccessibilityPlatformTranslation",
    "AccessibilitySharedSupport",
    "AccessibilityUI",
    "AccessibilityUIShared",
    "AccessibilityUIUtilities",
    "AccessibilityUIViewServices",
    "AccessibilityUtilities",
    "AccessoryAssistiveTouch",
    "AccessoryAudio",
    "AccessoryBLEPairing",
    "AccessoryCommunications",
    "AccessoryHID",
    "AccessoryMediaLibrary",
    "AccessoryNavigation",
    "AccessoryNowPlaying",
    "AccessoryOOBBTPairing",
    "AccessoryVoiceOver",
    "AccessoryiAP2Shim",
    "AccountNotification",
    "AccountSettings",
    "Accounts",
    "AccountsDaemon",
    "AccountsUI",
    "ActionKit",
    "ActionKitUI",
    "ActionPredictionHeuristics",
    "ActionPredictionHeuristicsInternal",
    "ActivityAchievements",
    "ActivityAchievementsDaemon",
    "ActivityAchievementsUI",
    "ActivityRingsUI",
    "ActivitySharing",
    "ActivitySharingUI",
    "AdAnalytics",
    "AdCore",
    "AdID",
    "AdPlatforms",
    "AdPlatformsInternal",
    "AdSupport",
    "AddressBook",
    "AddressBookLegacy",
    "AddressBookUI",
    "AggregateDictionaryHistory",
    "AirPlayReceiver",
    "AirPlayRoutePrediction",
    "AirPlaySender",
    "AirPlaySupport",
    "AirPortAssistant",
    "AirTraffic",
    "AirTrafficDevice",
    "AnnotationKit",
    "AppAnalytics",
    "AppConduit",
    "AppLaunchStats",
    "AppNotificationsLoggingClient",
    "AppPredictionClient",
    "AppPredictionInternal",
    "AppPredictionUI",
    "AppPredictionWidget",
    "AppPreferenceClient",
    "AppSSO",
    "AppSSOCore",
    "AppSSOKerberos",
    "AppSSOUI",
    "AppServerSupport",
    "AppStoreDaemon",
    "AppStoreFoundation",
    "AppStoreKit",
    "AppStoreUI",
    "AppSupport",
    "AppSupportUI",
    "AppleAccount",
    "AppleAccountUI",
    "AppleBasebandManager",
    "AppleCV3DMOVKit",
    "AppleCVA",
    "AppleCVAPhoto",
    "AppleIDAuthSupport",
    "AppleIDSSOAuthentication",
    "AppleLDAP",
    "AppleMediaServices",
    "AppleMediaServicesUI",
    "AppleNeuralEngine",
    "ApplePushService",
    "AppleServiceToolkit",
    "AskPermission",
    "AssertionServices",
    "AssetCacheServices",
    "AssetCacheServicesExtensions",
    "AssetExplorer",
    "AssetViewer",
    "AssetsLibrary",
    "AssetsLibraryServices",
    "AssistantCardServiceSupport",
    "AssistantServices",
    "AssistantSettingsSupport",
    "AssistantUI",
    "AttentionAwareness",
    "AudioDataAnalysis",
    "AudioPasscode",
    "AudioServerApplication",
    "AudioServerDriver",
    "AudioToolbox",
    "AudioToolboxCore",
    "AuthKit",
    "AuthKitUI",
    "AuthenticationServices",
    "AutoLoop",
    "AvatarKit",
    "AvatarUI",
    "BackBoardServices",
    "BackgroundTasks",
    "BarcodeSupport",
    "BaseBoard",
    "BaseBoardUI",
    "BatteryCenter",
    "BehaviorMiner",
    "BiometricKit",
    "BiometricKitUI",
    "BiometricSupport",
    "BluetoothAudio",
    "BluetoothManager",
    "BoardServices",
    "BookCoverUtility",
    "BookDataStore",
    "BookLibrary",
    "BookUtility",
    "BrailleTranslation",
    "BridgePreferences",
    "BulletinBoard",
    "BulletinDistributorCompanion",
    "BusinessChat",
    "BusinessChatService",
    "ButtonResolver",
    "C2",
    "CARDNDUI",
    "CDDataAccess",
    "CDDataAccessExpress",
    "CFNetwork",
    "CPMLBestShim",
    "CPMS",
    "CTCarrierSpace",
    "CTCarrierSpaceUI",
    "CacheDelete",
    "CalDAV",
    "Calculate",
    "CalendarDaemon",
    "CalendarDatabase",
    "CalendarFoundation",
    "CalendarNotification",
    "CalendarUIKit",
    "CallHistory",
    "CallKit",
    "CameraEditKit",
    "CameraEffectsKit",
    "CameraKit",
    "CameraUI",
    "CarKit",
    "CarPlay",
    "CarPlayServices",
    "CarPlaySupport",
    "CarPlayUIServices",
    "CardKit",
    "CardServices",
    "Cards",
    "Catalyst",
    "Categories",
    "Celestial",
    "CellularBridgeUI",
    "CellularPlanManager",
    "CertInfo",
    "CertUI",
    "ChatKit",
    "CheckerBoardServices",
    "ClassKit",
    "ClassKitUI",
    "ClassroomKit",
    "ClockComplications",
    "ClockKit",
    "ClockKitUI",
    "CloudDocs",
    "CloudDocsDaemon",
    "CloudDocsUI",
    "CloudKit",
    "CloudKitCode",
    "CloudKitCodeProtobuf",
    "CloudKitDaemon",
    "CloudPhotoLibrary",
    "CloudPhotoServices",
    "CloudServices",
    "Coherence",
    "Combine",
    "CommonUtilities",
    "CommunicationsFilter",
    "CommunicationsSetupUI",
    "CompanionCamera",
    "CompanionHealthDaemon",
    "CompanionSync",
    "CompassUI",
    "ConfigurationEngineModel",
    "ConstantClasses",
    "Contacts",
    "ContactsAssistantServices",
    "ContactsAutocomplete",
    "ContactsAutocompleteUI",
    "ContactsDonation",
    "ContactsDonationFeedback",
    "ContactsFoundation",
    "ContactsUI",
    "ContactsUICore",
    "ContentIndex",
    "ContentKit",
    "ContextKit",
    "ContinuousDialogManagerService",
    "ControlCenterServices",
    "ControlCenterUI",
    "ControlCenterUIKit",
    "ConversationKit",
    "CoreAccessories",
    "CoreAnalytics",
    "CoreAudio",
    "CoreAudioKit",
    "CoreBluetooth",
    "CoreBrightness",
    "CoreCDP",
    "CoreCDPInternal",
    "CoreCDPUI",
    "CoreCDPUIInternal",
    "CoreDAV",
    "CoreData",
    "CoreDuet",
    "CoreDuetContext",
    "CoreDuetDaemonProtocol",
    "CoreDuetDataModel",
    "CoreDuetDebugLogging",
    "CoreDuetStatistics",
    "CoreDuetSync",
    "CoreFollowUp",
    "CoreFollowUpUI",
    "CoreFoundation",
    "CoreHAP",
    "CoreHandwriting",
    "CoreHaptics",
    "CoreIDV",
    "CoreImage",
    "CoreIndoor",
    "CoreKnowledge",
    "CoreLocation",
    "CoreLocationProtobuf",
    "CoreMIDI",
    "CoreML",
    "CoreMaterial",
    "CoreMedia",
    "CoreMediaStream",
    "CoreMotion",
    "CoreNFC",
    "CoreNameParser",
    "CorePDF",
    "CorePrediction",
    "CoreRE",
    "CoreRecents",
    "CoreRecognition",
    "CoreRoutine",
    "CoreSDB",
    "CoreServices",
    "CoreServicesStore",
    "CoreSpeech",
    "CoreSpotlight",
    "CoreSuggestions",
    "CoreSuggestionsML",
    "CoreSuggestionsUI",
    "CoreTelephony",
    "CoreText",
    "CoreThemeDefinition",
    "CoreUI",
    "CoreUtils",
    "CoreUtilsSwift",
    "CoreWiFi",
    "CourseKit",
    "CoverSheet",
    "CrashReporterSupport",
    "CryptoKitCBridging",
    "CryptoKitPrivate",
    "CryptoTokenKit",
    "DAAPKit",
    "DAEASOAuthFramework",
    "DASActivitySchedulerUI",
    "DASDaemon",
    "DCIMServices",
    "DataAccess",
    "DataAccessExpress",
    "DataAccessUI",
    "DataDetectorsCore",
    "DataDetectorsNaturalLanguage",
    "DataDetectorsUI",
    "DataMigration",
    "DeviceCheck",
    "DeviceCheckInternal",
    "DeviceIdentity",
    "DeviceManagement",
    "DiagnosticExtensions",
    "DiagnosticExtensionsDaemon",
    "DiagnosticsKit",
    "DiagnosticsSupport",
    "DictionaryUI",
    "DifferentialPrivacy",
    "DigitalTouchShared",
    "DistributedEvaluation",
    "DoNotDisturb",
    "DoNotDisturbKit",
    "DoNotDisturbServer",
    "DocumentCamera",
    "DocumentManager",
    "DocumentManagerCore",
    "DocumentManagerExecutables",
    "DocumentManagerUICore",
    "DrawingKit",
    "DuetActivityScheduler",
    "DuetExpertCenter",
    "DuetRecommendation",
    "EAFirmwareUpdater",
    "EAP8021X",
    "EasyConfig",
    "EditScript",
    "Email",
    "EmailAddressing",
    "EmailCore",
    "EmailDaemon",
    "EmailFoundation",
    "EmbeddedAcousticRecognition",
    "EmbeddedDataReset",
    "EmergencyAlerts",
    "EmojiFoundation",
    "EmojiKit",
    "Engram",
    "EnhancedLoggingState",
    "Espresso",
    "EventKit",
    "EventKitUI",
    "ExchangeSync",
    "ExchangeSyncExpress",
    "ExternalAccessory",
    "FMClient",
    "FMCore",
    "FMCoreLite",
    "FMCoreUI",
    "FMF",
    "FMFCore",
    "FMFUI",
    "FMIPCore",
    "FMIPSiriActions",
    "FMNetworking",
    "FTClientServices",
    "FTServices",
    "FaceCore",
    "FamilyCircle",
    "FamilyCircleUI",
    "FamilyNotification",
    "FeatureFlagsSupport",
    "FileProvider",
    "FileProviderDaemon",
    "FileProviderUI",
    "FindMyDevice",
    "FindMyDeviceUI",
    "Fitness",
    "FitnessUI",
    "FlightUtilities",
    "FontServices",
    "FoundInAppsPlugins",
    "Foundation",
    "FriendKit",
    "FrontBoard",
    "FrontBoardServices",
    "FusionPluginKit",
    "FusionPluginServices",
    "Futhark",
    "GLKit",
    "GPURawCounter",
    "GameCenterFoundation",
    "GameController",
    "GameplayKit",
    "GenerationalStorage",
    "GeoServices",
    "GraphVisualizer",
    "HID",
    "HIDAnalytics",
    "HIDDisplay",
    "HMFoundation",
    "HSAAuthentication",
    "HangTracer",
    "Haptics",
    "HardwareDiagnostics",
    "HealthAlgorithms",
    "HealthDaemon",
    "HealthDiagnosticExtensionCore",
    "HealthEducationUI",
    "HealthExperience",
    "HealthExperienceUI",
    "HealthKit",
    "HealthKitUI",
    "HealthMenstrualCycles",
    "HealthMenstrualCyclesDaemon",
    "HealthMenstrualCyclesUI",
    "HealthOntology",
    "HealthPluginHost",
    "HealthProfile",
    "HealthRecordServices",
    "HealthRecordsUI",
    "HealthToolbox",
    "HealthUI",
    "HealthVisualization",
    "HearingCore",
    "HearingUI",
    "HearingUtilities",
    "HeartRhythmUI",
    "HelpKit",
    "HeroAppPredictionClient",
    "Home",
    "HomeAI",
    "HomeKit",
    "HomeKitBackingStore",
    "HomeKitDaemon",
    "HomeSharing",
    "HomeUI",
    "IAP",
    "IDS",
    "IDSFoundation",
    "IDSHashPersistence",
    "IDSKVStore",
    "IMAVCore",
    "IMAssistantCore",
    "IMCore",
    "IMDMessageServices",
    "IMDPersistence",
    "IMDaemonCore",
    "IMFoundation",
    "IMSharedUI",
    "IMSharedUtilities",
    "IMTranscoderAgent",
    "IMTranscoding",
    "IMTransferAgent",
    "IMTransferServices",
    "IOAccelMemoryInfo",
    "IOAccelerator",
    "IOAccessoryManager",
    "IOKit",
    "IOSurface",
    "IOUSBHost",
    "IPTelephony",
    "ITMLKit",
    "IconServices",
    "IdentityLookup",
    "IdentityLookupUI",
    "IdleTimerServices",
    "ImageCaptureCore",
    "InAppMessages",
    "InCallService",
    "IncomingCallFilter",
    "InertiaCam",
    "InfoKit",
    "InputContext",
    "InstallCoordination",
    "Intents",
    "IntentsCore",
    "IntentsFoundation",
    "IntentsServices",
    "IntentsUI",
    "IntentsUICardKitProviderSupport",
    "InternationalSupport",
    "IntlPreferences",
    "JITAppKit",
    "JetEngine",
    "JetUI",
    "KeyboardArbiter",
    "KeyboardServices",
    "KeychainCircle",
    "KnowledgeGraphKit",
    "KnowledgeMonitor",
    "LimitAdTracking",
    "LinguisticData",
    "LinkPresentation",
    "LiveFS",
    "LiveFSFPHelper",
    "LocalAuthentication",
    "LocalAuthenticationPrivateUI",
    "LocationSupport",
    "LockoutUI",
    "LoggingSupport",
    "LoginKit",
    "LoginUILogViewer",
    "MDM",
    "MFAAuthentication",
    "MIME",
    "MMCS",
    "MMCSServices",
    "MOVStreamIO",
    "MPUFoundation",
    "MailServices",
    "MailSupport",
    "MailWebProcessSupport",
    "ManagedConfiguration",
    "ManagedConfigurationUI",
    "MapKit",
    "MapsSuggestions",
    "MapsSupport",
    "MarkupUI",
    "MaterialKit",
    "MediaControlSender",
    "MediaControls",
    "MediaConversionService",
    "MediaExperience",
    "MediaMiningKit",
    "MediaPlaybackCore",
    "MediaPlayer",
    "MediaPlayerUI",
    "MediaRemote",
    "MediaServices",
    "MediaStream",
    "MediaToolbox",
    "Memories",
    "Message",
    "MessageLegacy",
    "MessageProtection",
    "MessageSecurity",
    "MessageUI",
    "Messages",
    "MetadataUtilities",
    "Metal",
    "MetalKit",
    "MetalPerformanceShaders",
    "MetalTools",
    "MetricKit",
    "MetricKitCore",
    "MetricKitServices",
    "MetricKitSource",
    "MetricMeasurement",
    "MetricsKit",
    "MobileAccessoryUpdater",
    "MobileActivation",
    "MobileAsset",
    "MobileAssetUpdater",
    "MobileBackup",
    "MobileContainerManager",
    "MobileIcons",
    "MobileInstallation",
    "MobileKeyBag",
    "MobileLookup",
    "MobileMailUI",
    "MobileSoftwareUpdate",
    "MobileStorage",
    "MobileStoreDemoKit",
    "MobileSystemServices",
    "MobileTimer",
    "MobileTimerUI",
    "MobileWiFi",
    "ModelIO",
    "Montreal",
    "MultipeerConnectivity",
    "MusicCarDisplayUI",
    "MusicLibrary",
    "MusicStoreUI",
    "NCLaunchStats",
    "NLFoundInAppsPlugin",
    "NLP",
    "NLPLearner",
    "NanoAppRegistry",
    "NanoAudioControl",
    "NanoBackup",
    "NanoComplicationSettings",
    "NanoLeash",
    "NanoMailKitServer",
    "NanoMediaBridgeUI",
    "NanoMediaRemote",
    "NanoMusicSync",
    "NanoPassKit",
    "NanoPhonePerfTesting",
    "NanoPreferencesSync",
    "NanoRegistry",
    "NanoResourceGrabber",
    "NanoSystemSettings",
    "NanoTimeKitCompanion",
    "NanoUniverse",
    "NanoWeatherComplicationsCompanion",
    "NaturalLanguage",
    "Navigation",
    "NearField",
    "NetAppsUtilities",
    "NetAppsUtilitiesUI",
    "Network",
    "NetworkExtension",
    "NetworkRelay",
    "NetworkServiceProxy",
    "NetworkStatistics",
    "NeutrinoCore",
    "NeutrinoKit",
    "NewDeviceOutreach",
    "NewDeviceOutreachUI",
    "NewsAnalytics",
    "NewsAnalyticsUpload",
    "NewsArticles",
    "NewsCore",
    "NewsDaemon",
    "NewsFeed",
    "NewsFeedLayout",
    "NewsFoundation",
    "NewsServices",
    "NewsServicesInternal",
    "NewsSubscription",
    "NewsToday",
    "NewsTransport",
    "NewsUI",
    "NewsUI2",
    "NewsstandKit",
    "Notes",
    "NotesShared",
    "NotesUI",
    "NotificationCenter",
    "OAuth",
    "OSAServicesClient",
    "OSASubmissionClient",
    "OSASyncProxyClient",
    "OSAnalytics",
    "OSAnalyticsPrivate",
    "OTSVG",
    "OfficeImport",
    "OnBoardingKit",
    "OpenGLES",
    "Osprey",
    "PASampling",
    "PBBridgeSupport",
    "PDFKit",
    "PLSnapshot",
    "PairedSync",
    "PairedUnlock",
    "PairingProximity",
    "PassKit",
    "PassKitCore",
    "PassKitUI",
    "PassKitUIFoundation",
    "Pasteboard",
    "Pegasus",
    "PencilKit",
    "PencilPairingUI",
    "PeopleSuggester",
    "PersistentConnection",
    "PersonaKit",
    "PersonaUI",
    "PersonalizationPortrait",
    "PersonalizationPortraitInternals",
    "PhotoAnalysis",
    "PhotoBoothEffects",
    "PhotoFoundation",
    "PhotoImaging",
    "PhotoLibrary",
    "PhotoLibraryServices",
    "PhotoVision",
    "Photos",
    "PhotosFormats",
    "PhotosGraph",
    "PhotosImagingFoundation",
    "PhotosPlayer",
    "PhysicsKit",
    "PipelineKit",
    "PlacesKit",
    "PlatterKit",
    "PlugInKit",
    "PodcastsKit",
    "PowerLog",
    "PowerUI",
    "Preferences",
    "PreferencesUI",
    "PrintKit",
    "PrivateFederatedLearning",
    "ProVideo",
    "ProactiveEventTracker",
    "ProactiveExperiments",
    "ProactiveExperimentsInternals",
    "ProactiveML",
    "ProactiveMagicalMoments",
    "ProactiveSupport",
    "ProactiveSupportStubs",
    "ProactiveWidgetTracker",
    "ProgressUI",
    "ProofReader",
    "ProtectedCloudStorage",
    "ProtocolBuffer",
    "PrototypeTools",
    "PrototypeToolsUI",
    "Proximity",
    "PushKit",
    "QLCharts",
    "QuartzCore",
    "QuickLook",
    "QuickLookSupport",
    "QuickLookThumbnailing",
    "ROCKit",
    "RTCReporting",
    "RTTUI",
    "RTTUtilities",
    "Radio",
    "Rapport",
    "RapportUI",
    "RealityKit",
    "RelevanceEngine",
    "RelevanceEngineUI",
    "ReminderKit",
    "ReminderKitUI",
    "ReminderMigration",
    "RemindersUI",
    "RemoteConfiguration",
    "RemoteCoreML",
    "RemoteManagement",
    "RemoteMediaServices",
    "RemoteServiceDiscovery",
    "RemoteStateDumpKit",
    "RemoteTextInput",
    "RemoteUI",
    "RemoteXPC",
    "RenderBox",
    "ReplayKit",
    "ResponseKit",
    "RevealCore",
    "RunningBoard",
    "RunningBoardServices",
    "SAML",
    "SAObjects",
    "SEService",
    "SIMSetupSupport",
    "SIMToolkitUI",
    "SMBClientEngine",
    "SMBClientProvider",
    "SMBSearch",
    "SOS",
    "SPFinder",
    "SPOwner",
    "SPShared",
    "SafariCore",
    "SafariFoundation",
    "SafariSafeBrowsing",
    "SafariServices",
    "SafariShared",
    "SampleAnalysis",
    "SceneKit",
    "ScreenReaderBrailleDriver",
    "ScreenReaderCore",
    "ScreenReaderOutput",
    "ScreenTimeCore",
    "ScreenTimeUI",
    "ScreenshotServices",
    "Search",
    "SearchAds",
    "SearchFoundation",
    "SearchUI",
    "SearchUICardKitProviderSupport",
    "SecureChannel",
    "Security",
    "SecurityFoundation",
    "SensingProtocols",
    "SensorKit",
    "SensorKitUI",
    "Sentry",
    "SettingsCellular",
    "SettingsCellularUI",
    "SettingsFoundation",
    "SetupAssistant",
    "SetupAssistantSupport",
    "SetupAssistantUI",
    "ShareSheet",
    "SharedWebCredentials",
    "Sharing",
    "SharingUI",
    "ShortcutUIKit",
    "SidecarCore",
    "SidecarUI",
    "SignpostCollection",
    "SignpostMetrics",
    "SignpostSupport",
    "Silex",
    "SilexText",
    "SilexVideo",
    "SiriActivation",
    "SiriClientFlow",
    "SiriCore",
    "SiriInstrumentation",
    "SiriTape",
    "SiriTasks",
    "SiriUI",
    "SiriUIActivation",
    "SiriUICardKitProviderSupport",
    "SiriUICore",
    "SlideshowKit",
    "Social",
    "SocialServices",
    "SoftwareUpdateBridge",
    "SoftwareUpdateCore",
    "SoftwareUpdateCoreSupport",
    "SoftwareUpdateServices",
    "SoftwareUpdateServicesUI",
    "SoftwareUpdateSettings",
    "SoftwareUpdateSettingsUI",
    "SoundAnalysis",
    "SoundAutoConfig",
    "SoundBoardServices",
    "SpeakThisServices",
    "SpeakTypingServices",
    "Speech",
    "SpeechRecognitionCommandAndControl",
    "SpeechRecognitionCommandServices",
    "SplashBoard",
    "Spotlight",
    "SpotlightDaemon",
    "SpotlightReceiver",
    "SpotlightServices",
    "SpotlightUI",
    "SpotlightUIInternal",
    "SpringBoardFoundation",
    "SpringBoardHome",
    "SpringBoardServices",
    "SpringBoardUI",
    "SpringBoardUIServices",
    "SpriteKit",
    "StarBoardFoundation",
    "StarBoardServices",
    "Stocks",
    "StorageSettings",
    "StoreBookkeeper",
    "StoreBookkeeperClient",
    "StoreKit",
    "StoreKitUI",
    "StoreServices",
    "StreamingZip",
    "StudyLog",
    "SuggestionsSpotlightMetrics",
    "SwiftUI",
    "Symbolication",
    "SymptomDiagnosticReporter",
    "Symptoms",
    "SyncedDefaults",
    "SystemStatus",
    "SystemStatusServer",
    "TSReading",
    "TSUtility",
    "TVLatency",
    "TVMLKit",
    "TVPlayback",
    "TVRemoteCore",
    "TVRemoteKit",
    "TVRemoteUI",
    "TVUIKit",
    "TeaCharts",
    "TeaDB",
    "TeaFoundation",
    "TeaSettings",
    "TeaTemplate",
    "TeaUI",
    "TelephonyPreferences",
    "TelephonyRPC",
    "TelephonyUI",
    "TelephonyUtilities",
    "TemplateKit",
    "TestFlightCore",
    "TextInput",
    "TextInputChinese",
    "TextInputCore",
    "TextInputUI",
    "TextRecognition",
    "TextToSpeech",
    "TextureIO",
    "TimeSync",
    "TinCanShared",
    "Tips",
    "ToneKit",
    "ToneLibrary",
    "TouchML",
    "TouchRemote",
    "TrackingAvoidance",
    "Transparency",
    "TransparencyDetailsView",
    "Trial",
    "TrialProto",
    "TrialServer",
    "TrustedPeers",
    "Twitter",
    "UIAccessibility",
    "UIFoundation",
    "UIKitCore",
    "UIKitServices",
    "UITriggerVC",
    "URLFormatting",
    "USDKit",
    "UpNextWidget",
    "UsageTracking",
    "UserActivity",
    "UserFS",
    "UserManagement",
    "UserNotifications",
    "UserNotificationsKit",
    "UserNotificationsServer",
    "UserNotificationsSettings",
    "UserNotificationsUI",
    "UserNotificationsUIKit",
    "VideoProcessing",
    "VideoSubscriberAccount",
    "VideoSubscriberAccountUI",
    "VideoToolbox",
    "VideosUI",
    "VideosUICore",
    "Vision",
    "VisionKit",
    "VisualAlert",
    "VisualPairing",
    "VoiceMemos",
    "VoiceOverServices",
    "VoiceServices",
    "VoiceShortcutClient",
    "VoiceShortcuts",
    "VoiceShortcutsUI",
    "VoiceTrigger",
    "VoiceTriggerUI",
    "WPDaemon",
    "WallpaperKit",
    "WatchConnectivity",
    "WatchKit",
    "WatchListKit",
    "WatchReplies",
    "Weather",
    "WeatherFoundation",
    "WeatherUI",
    "WebApp",
    "WebBookmarks",
    "WebContentAnalysis",
    "WebCore",
    "WebInspector",
    "WebKit",
    "WebUI",
    "WelcomeKit",
    "WelcomeKitCore",
    "WelcomeKitUI",
    "WiFiAnalytics",
    "WiFiCloudSyncEngine",
    "WiFiKit",
    "WiFiKitUI",
    "WiFiLogCapture",
    "WiFiPolicy",
    "WiFiVelocity",
    "Widgets",
    "WirelessCoexManager",
    "WirelessDiagnostics",
    "WirelessProximity",
    "WorkflowKit",
    "WorkflowUI",
    "XCTTargetBootstrap",
    "ZoomServices",
    "iAd",
    "iAdCore",
    "iAdDeveloper",
    "iAdServices",
    "iCalendar",
    "iCloudNotification",
    "iCloudQuota",
    "iCloudQuotaDaemon",
    "iCloudQuotaUI",
    "iMessageApps",
    "iOSDiagnostics",
    "iOSScreenSharing",
    "iTunesCloud",
    "iTunesStore",
    "iTunesStoreUI",
    "perfdata",
    "vCard",
]
#downloadOnly = downloadAll
downloadOnly = [ "ABMHelper" ]
downloadPath = "./Headers"
verifySsl = True
if not verifySsl:
    urllib3.disable_warnings()

mainPageLink = "http://developer.limneos.net/index.php?ios={}"
downloadPageLink = "http://developer.limneos.net/headers/{}/{}/Headers/{}"
frameworkLinkRegex = "\?ios=.*&framework=(.*)"
headerLinkRegex = "\?ios=.*&framework=.*&header=(.*)"

main = mainPageLink.format(iosVersion)

page = requests.get(main, verify=verifySsl)
tree = html.fromstring(page.content)

frameworks = tree.xpath('/html/body/div[@id="container"]/div/a/@href')

headerDownloads = []
for frameworkLink in frameworks:
    frameworkName = re.search(frameworkLinkRegex, frameworkLink)
    frameworkName = frameworkName.group(1) if frameworkName is not None else None
    if frameworkName.replace(".framework", "") not in downloadOnly and len(downloadOnly) != 0: continue

    frameworkPage = requests.get(main.split("?")[0] + frameworkLink, verify=verifySsl)
    frameworkTree = html.fromstring(frameworkPage.content)

    headers = frameworkTree.xpath('/html/body/div[@id="container"]/div/a/@href')

    for headerLink in headers:
        headerFileName = re.search(headerLinkRegex, headerLink)
        headerFileName = headerFileName.group(1) if headerFileName is not None else None

        if headerFileName is None: continue
    
        headerDownloads.append([frameworkName, headerFileName])

numOfDownloads = len(headerDownloads)
maxDigits = str(len(str(numOfDownloads)))
progressStringFormat = "{:" + maxDigits + "d}/{:" + maxDigits + "d}"
stringFormat = "(" + progressStringFormat + ") {:13}:{} - {}"

for i in range(len(headerDownloads)):
    download = headerDownloads[i]
    downloadLink = downloadPageLink.format(iosVersion, download[0], download[1])
    savePath = os.path.join(downloadPath, download[0], download[1])
    if os.path.isfile(savePath):
        print(stringFormat.format(i, numOfDownloads, "Skipping", download[0], download[1]));
        continue
    else:
        createDir(os.path.join(downloadPath, download[0]))
        print(stringFormat.format(i, numOfDownloads, "Downloading", download[0], download[1]));

    r = requests.get(downloadLink, verify=verifySsl) 
    with open(savePath, 'wb') as out:
        out.write(r.content)
