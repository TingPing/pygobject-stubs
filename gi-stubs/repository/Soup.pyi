
from typing import Any
from typing import Callable
from typing import Optional
from typing import overload

from gi.repository import GLib
from gi.repository import Gio
from gi.repository import GObject


SessionCallbackU = Callable[[Session, Message, Any], None]
SessionCallback = Callable[[Session, Message], None]


ADDRESS_ANY_PORT = ...
ADDRESS_FAMILY: str = ...
ADDRESS_NAME: str = ...
ADDRESS_PHYSICAL: str = ...
ADDRESS_PORT: str = ...
ADDRESS_PROTOCOL: str = ...
ADDRESS_SOCKADDR: str = ...
AUTH_DOMAIN_ADD_PATH: str = ...
AUTH_DOMAIN_BASIC_AUTH_CALLBACK: str = ...
AUTH_DOMAIN_BASIC_AUTH_DATA: str = ...
AUTH_DOMAIN_DIGEST_AUTH_CALLBACK: str = ...
AUTH_DOMAIN_DIGEST_AUTH_DATA: str = ...
AUTH_DOMAIN_FILTER: str = ...
AUTH_DOMAIN_FILTER_DATA: str = ...
AUTH_DOMAIN_GENERIC_AUTH_CALLBACK: str = ...
AUTH_DOMAIN_GENERIC_AUTH_DATA: str = ...
AUTH_DOMAIN_PROXY: str = ...
AUTH_DOMAIN_REALM: str = ...
AUTH_DOMAIN_REMOVE_PATH: str = ...
AUTH_HOST: str = ...
AUTH_IS_AUTHENTICATED: str = ...
AUTH_IS_FOR_PROXY: str = ...
AUTH_REALM: str = ...
AUTH_SCHEME_NAME: str = ...
CHAR_HTTP_CTL: int = ...
CHAR_HTTP_SEPARATOR: int = ...
CHAR_URI_GEN_DELIMS: int = ...
CHAR_URI_PERCENT_ENCODED: int = ...
CHAR_URI_SUB_DELIMS: int = ...
COOKIE_JAR_ACCEPT_POLICY: str = ...
COOKIE_JAR_DB_FILENAME: str = ...
COOKIE_JAR_READ_ONLY: str = ...
COOKIE_JAR_TEXT_FILENAME: str = ...
COOKIE_MAX_AGE_ONE_DAY = ...
COOKIE_MAX_AGE_ONE_HOUR: int = ...
COOKIE_MAX_AGE_ONE_WEEK = ...
COOKIE_MAX_AGE_ONE_YEAR = ...
FORM_MIME_TYPE_MULTIPART: str = ...
FORM_MIME_TYPE_URLENCODED: str = ...
HSTS_ENFORCER_DB_FILENAME: str = ...
HSTS_POLICY_MAX_AGE_PAST = ...
LOGGER_LEVEL: str = ...
LOGGER_MAX_BODY_SIZE: str = ...
MAJOR_VERSION: int = ...
MESSAGE_FIRST_PARTY: str = ...
MESSAGE_FLAGS: str = ...
MESSAGE_HTTP_VERSION: str = ...
MESSAGE_IS_TOP_LEVEL_NAVIGATION: str = ...
MESSAGE_METHOD: str = ...
MESSAGE_PRIORITY: str = ...
MESSAGE_REASON_PHRASE: str = ...
MESSAGE_REQUEST_BODY: str = ...
MESSAGE_REQUEST_BODY_DATA: str = ...
MESSAGE_REQUEST_HEADERS: str = ...
MESSAGE_RESPONSE_BODY: str = ...
MESSAGE_RESPONSE_BODY_DATA: str = ...
MESSAGE_RESPONSE_HEADERS: str = ...
MESSAGE_SERVER_SIDE: str = ...
MESSAGE_SITE_FOR_COOKIES: str = ...
MESSAGE_STATUS_CODE: str = ...
MESSAGE_TLS_CERTIFICATE: str = ...
MESSAGE_TLS_ERRORS: str = ...
MESSAGE_URI: str = ...
MICRO_VERSION = ...
MINOR_VERSION: int = ...
REQUEST_SESSION: str = ...
REQUEST_URI: str = ...
SERVER_ASYNC_CONTEXT: str = ...
SERVER_HTTPS_ALIASES: str = ...
SERVER_HTTP_ALIASES: str = ...
SERVER_INTERFACE: str = ...
SERVER_PORT: str = ...
SERVER_RAW_PATHS: str = ...
SERVER_SERVER_HEADER: str = ...
SERVER_SSL_CERT_FILE: str = ...
SERVER_SSL_KEY_FILE: str = ...
SERVER_TLS_CERTIFICATE: str = ...
SESSION_ACCEPT_LANGUAGE: str = ...
SESSION_ACCEPT_LANGUAGE_AUTO: str = ...
SESSION_ASYNC_CONTEXT: str = ...
SESSION_HTTPS_ALIASES: str = ...
SESSION_HTTP_ALIASES: str = ...
SESSION_IDLE_TIMEOUT: str = ...
SESSION_LOCAL_ADDRESS: str = ...
SESSION_MAX_CONNS: str = ...
SESSION_MAX_CONNS_PER_HOST: str = ...
SESSION_PROXY_RESOLVER: str = ...
SESSION_PROXY_URI: str = ...
SESSION_SSL_CA_FILE: str = ...
SESSION_SSL_STRICT: str = ...
SESSION_SSL_USE_SYSTEM_CA_FILE: str = ...
SESSION_TIMEOUT: str = ...
SESSION_TLS_DATABASE: str = ...
SESSION_TLS_INTERACTION: str = ...
SESSION_USER_AGENT: str = ...
SESSION_USE_NTLM: str = ...
SESSION_USE_THREAD_CONTEXT: str = ...
SOCKET_ASYNC_CONTEXT: str = ...
SOCKET_FLAG_NONBLOCKING: str = ...
SOCKET_IS_SERVER: str = ...
SOCKET_LOCAL_ADDRESS: str = ...
SOCKET_REMOTE_ADDRESS: str = ...
SOCKET_SSL_CREDENTIALS: str = ...
SOCKET_SSL_FALLBACK: str = ...
SOCKET_SSL_STRICT: str = ...
SOCKET_TIMEOUT: str = ...
SOCKET_TLS_CERTIFICATE: str = ...
SOCKET_TLS_ERRORS: str = ...
SOCKET_TRUSTED_CERTIFICATE: str = ...
SOCKET_USE_THREAD_CONTEXT: str = ...
VERSION_MIN_REQUIRED: int = ...
_namespace: str = ...
_version: str = ...

def check_version(*args, **kwargs): ...
def cookie_parse(*args, **kwargs): ...
def cookies_from_request(*args, **kwargs): ...
def cookies_from_response(*args, **kwargs): ...
def cookies_to_cookie_header(*args, **kwargs): ...
def cookies_to_request(*args, **kwargs): ...
def cookies_to_response(*args, **kwargs): ...
def form_decode(*args, **kwargs): ...
def form_decode_multipart(*args, **kwargs): ...
def form_encode_datalist(*args, **kwargs): ...
def form_encode_hash(*args, **kwargs): ...
def form_request_new_from_datalist(*args, **kwargs): ...
def form_request_new_from_hash(*args, **kwargs): ...
def form_request_new_from_multipart(*args, **kwargs): ...
def get_major_version(*args, **kwargs): ...
def get_micro_version(*args, **kwargs): ...
def get_minor_version(*args, **kwargs): ...
def get_resource(*args, **kwargs): ...
def header_contains(*args, **kwargs): ...
def header_free_param_list(*args, **kwargs): ...
def header_g_string_append_param(*args, **kwargs): ...
def header_g_string_append_param_quoted(*args, **kwargs): ...
def header_parse_list(*args, **kwargs): ...
def header_parse_param_list(*args, **kwargs): ...
def header_parse_param_list_strict(*args, **kwargs): ...
def header_parse_quality_list(*args, **kwargs): ...
def header_parse_semi_param_list(*args, **kwargs): ...
def header_parse_semi_param_list_strict(*args, **kwargs): ...
def headers_parse(*args, **kwargs): ...
def headers_parse_request(*args, **kwargs): ...
def headers_parse_response(*args, **kwargs): ...
def headers_parse_status_line(*args, **kwargs): ...
def http_error_quark(*args, **kwargs): ...
def message_headers_iter_init(*args, **kwargs): ...
def request_error_quark(*args, **kwargs): ...
def requester_error_quark(*args, **kwargs): ...
def status_get_phrase(*args, **kwargs): ...
def status_proxify(*args, **kwargs): ...
def str_case_equal(*args, **kwargs): ...
def str_case_hash(*args, **kwargs): ...
def tld_domain_is_public_suffix(*args, **kwargs): ...
def tld_error_quark(*args, **kwargs): ...
def tld_get_base_domain(*args, **kwargs): ...
def uri_decode(*args, **kwargs): ...
def uri_encode(*args, **kwargs): ...
def uri_normalize(*args, **kwargs): ...
def value_array_new(*args, **kwargs): ...
def value_hash_insert_value(*args, **kwargs): ...
def value_hash_new(*args, **kwargs): ...
def websocket_client_prepare_handshake(*args, **kwargs): ...
def websocket_client_prepare_handshake_with_extensions(*args, **kwargs): ...
def websocket_client_verify_handshake(*args, **kwargs): ...
def websocket_client_verify_handshake_with_extensions(*args, **kwargs): ...
def websocket_error_get_quark(*args, **kwargs): ...
def websocket_server_check_handshake(*args, **kwargs): ...
def websocket_server_check_handshake_with_extensions(*args, **kwargs): ...
def websocket_server_process_handshake(*args, **kwargs): ...
def websocket_server_process_handshake_with_extensions(*args, **kwargs): ...
def xmlrpc_build_method_call(*args, **kwargs): ...
def xmlrpc_build_method_response(*args, **kwargs): ...
def xmlrpc_build_request(*args, **kwargs): ...
def xmlrpc_build_response(*args, **kwargs): ...
def xmlrpc_error_quark(*args, **kwargs): ...
def xmlrpc_fault_quark(*args, **kwargs): ...
def xmlrpc_message_new(*args, **kwargs): ...
def xmlrpc_message_set_response(*args, **kwargs): ...
def xmlrpc_parse_method_call(*args, **kwargs): ...
def xmlrpc_parse_method_response(*args, **kwargs): ...
def xmlrpc_parse_request(*args, **kwargs): ...
def xmlrpc_parse_response(*args, **kwargs): ...
def xmlrpc_variant_get_datetime(*args, **kwargs): ...
def xmlrpc_variant_new_datetime(*args, **kwargs): ...

class Address:
    parent = ...
    
    def equal_by_ip(*args, **kwargs): ...
    def equal_by_name(*args, **kwargs): ...
    def get_gsockaddr(*args, **kwargs): ...
    def get_name(*args, **kwargs): ...
    def get_physical(*args, **kwargs): ...
    def get_port(*args, **kwargs): ...
    def get_sockaddr(*args, **kwargs): ...
    def hash_by_ip(*args, **kwargs): ...
    def hash_by_name(*args, **kwargs): ...
    def is_resolved(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_any(*args, **kwargs): ...
    def new_from_sockaddr(*args, **kwargs): ...
    def resolve_async(*args, **kwargs): ...
    def resolve_sync(*args, **kwargs): ...
    

class Auth:
    parent = ...
    realm = ...
    
    def authenticate(*args, **kwargs): ...
    def can_authenticate(*args, **kwargs): ...
    def get_authorization(*args, **kwargs): ...
    def get_host(*args, **kwargs): ...
    def get_info(*args, **kwargs): ...
    def get_protection_space(*args, **kwargs): ...
    def get_realm(*args, **kwargs): ...
    def get_saved_password(*args, **kwargs): ...
    def get_saved_users(*args, **kwargs): ...
    def get_scheme_name(*args, **kwargs): ...
    def has_saved_password(*args, **kwargs): ...
    def is_authenticated(*args, **kwargs): ...
    def is_for_proxy(*args, **kwargs): ...
    def is_ready(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def save_password(*args, **kwargs): ...
    def update(*args, **kwargs): ...
    
    def do_authenticate(self, *args, **kwargs): ...
    def do_can_authenticate(self, *args, **kwargs): ...
    def do_get_authorization(self, *args, **kwargs): ...
    def do_get_protection_space(self, *args, **kwargs): ...
    def do_is_authenticated(self, *args, **kwargs): ...
    def do_is_ready(self, *args, **kwargs): ...
    def do_update(self, *args, **kwargs): ...
    

class AuthBasic: ...

class AuthDigest: ...

class AuthDomain:
    parent = ...
    
    def accepts(*args, **kwargs): ...
    def add_path(*args, **kwargs): ...
    def challenge(*args, **kwargs): ...
    def check_password(*args, **kwargs): ...
    def covers(*args, **kwargs): ...
    def get_realm(*args, **kwargs): ...
    def remove_path(*args, **kwargs): ...
    def set_filter(*args, **kwargs): ...
    def set_generic_auth_callback(*args, **kwargs): ...
    def try_generic_auth_callback(*args, **kwargs): ...
    
    def do_accepts(self, *args, **kwargs): ...
    def do_challenge(self, *args, **kwargs): ...
    def do_check_password(self, *args, **kwargs): ...
    

class AuthDomainBasic:
    def set_auth_callback(*args, **kwargs): ...
    

class AuthDomainDigest:
    def encode_password(*args, **kwargs): ...
    def set_auth_callback(*args, **kwargs): ...
    

class AuthManager:
    parent = ...
    priv = ...
    
    def clear_cached_credentials(*args, **kwargs): ...
    def use_auth(*args, **kwargs): ...
    
    def do_authenticate(self, *args, **kwargs): ...
    

class AuthNTLM: ...

class AuthNegotiate:
    def supported(*args, **kwargs): ...
    

class Buffer:
    data = ...
    length = ...
    
    def free(*args, **kwargs): ...
    def get_as_bytes(*args, **kwargs): ...
    def get_data(self) -> bytes: ...
    def get_owner(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_subbuffer(*args, **kwargs): ...
    def new_with_owner(*args, **kwargs): ...
    

class ByteArray: ...

class Cache:
    parent_instance = ...
    priv = ...
    
    def clear(*args, **kwargs): ...
    def dump(*args, **kwargs): ...
    def flush(*args, **kwargs): ...
    def get_max_size(*args, **kwargs): ...
    def load(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_max_size(*args, **kwargs): ...
    
    def do_get_cacheability(self, *args, **kwargs): ...
    

class ClientContext:
    def get_address(*args, **kwargs): ...
    def get_auth_domain(*args, **kwargs): ...
    def get_auth_user(*args, **kwargs): ...
    def get_gsocket(*args, **kwargs): ...
    def get_host(*args, **kwargs): ...
    def get_local_address(*args, **kwargs): ...
    def get_remote_address(*args, **kwargs): ...
    def get_socket(*args, **kwargs): ...
    def steal_connection(*args, **kwargs): ...
    

class Connection: ...

class ContentDecoder:
    parent = ...
    priv = ...
    

class ContentSniffer(GObject.Object, SessionFeature):
    parent = ...
    priv = ...
    
    def get_buffer_size(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def sniff(*args, **kwargs): ...
    
    def do_get_buffer_size(self, *args, **kwargs): ...
    def do_sniff(self, *args, **kwargs): ...
    

class Cookie:
    domain = ...
    expires = ...
    http_only = ...
    name = ...
    path = ...
    secure = ...
    value = ...
    
    def applies_to_uri(*args, **kwargs): ...
    def domain_matches(*args, **kwargs): ...
    def equal(*args, **kwargs): ...
    def free(*args, **kwargs): ...
    def get_domain(*args, **kwargs): ...
    def get_expires(*args, **kwargs): ...
    def get_http_only(*args, **kwargs): ...
    def get_name(*args, **kwargs): ...
    def get_path(*args, **kwargs): ...
    def get_same_site_policy(*args, **kwargs): ...
    def get_secure(*args, **kwargs): ...
    def get_value(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def parse(*args, **kwargs): ...
    def set_domain(*args, **kwargs): ...
    def set_expires(*args, **kwargs): ...
    def set_http_only(*args, **kwargs): ...
    def set_max_age(*args, **kwargs): ...
    def set_name(*args, **kwargs): ...
    def set_path(*args, **kwargs): ...
    def set_same_site_policy(*args, **kwargs): ...
    def set_secure(*args, **kwargs): ...
    def set_value(*args, **kwargs): ...
    def to_cookie_header(*args, **kwargs): ...
    def to_set_cookie_header(*args, **kwargs): ...
    

class CookieJar:
    parent = ...
    
    def add_cookie(*args, **kwargs): ...
    def add_cookie_full(*args, **kwargs): ...
    def add_cookie_with_first_party(*args, **kwargs): ...
    def all_cookies(*args, **kwargs): ...
    def delete_cookie(*args, **kwargs): ...
    def get_accept_policy(*args, **kwargs): ...
    def get_cookie_list(*args, **kwargs): ...
    def get_cookie_list_with_same_site_info(*args, **kwargs): ...
    def get_cookies(*args, **kwargs): ...
    def is_persistent(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def save(*args, **kwargs): ...
    def set_accept_policy(*args, **kwargs): ...
    def set_cookie(*args, **kwargs): ...
    def set_cookie_with_first_party(*args, **kwargs): ...
    
    def do_changed(self, *args, **kwargs): ...
    def do_is_persistent(self, *args, **kwargs): ...
    def do_save(self, *args, **kwargs): ...
    

class CookieJarDB: ...

class CookieJarText: ...

class Date:
    day = ...
    hour = ...
    minute = ...
    month = ...
    offset = ...
    second = ...
    utc = ...
    year = ...
    
    def free(*args, **kwargs): ...
    def get_day(*args, **kwargs): ...
    def get_hour(*args, **kwargs): ...
    def get_minute(*args, **kwargs): ...
    def get_month(*args, **kwargs): ...
    def get_offset(*args, **kwargs): ...
    def get_second(*args, **kwargs): ...
    def get_utc(*args, **kwargs): ...
    def get_year(*args, **kwargs): ...
    def is_past(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_from_now(*args, **kwargs): ...
    def new_from_string(*args, **kwargs): ...
    def new_from_time_t(*args, **kwargs): ...
    def to_string(*args, **kwargs): ...
    def to_time_t(*args, **kwargs): ...
    def to_timeval(*args, **kwargs): ...
    

class HSTSEnforcer:
    parent = ...
    priv = ...
    
    def get_domains(*args, **kwargs): ...
    def get_policies(*args, **kwargs): ...
    def has_valid_policy(*args, **kwargs): ...
    def is_persistent(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_policy(*args, **kwargs): ...
    def set_session_policy(*args, **kwargs): ...
    
    def do_changed(self, *args, **kwargs): ...
    def do_has_valid_policy(self, *args, **kwargs): ...
    def do_hsts_enforced(self, *args, **kwargs): ...
    def do_is_persistent(self, *args, **kwargs): ...
    

class HSTSEnforcerDB: ...

class HSTSPolicy:
    domain = ...
    expires = ...
    include_subdomains = ...
    max_age = ...
    
    def equal(*args, **kwargs): ...
    def free(*args, **kwargs): ...
    def get_domain(*args, **kwargs): ...
    def includes_subdomains(*args, **kwargs): ...
    def is_expired(*args, **kwargs): ...
    def is_session_policy(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_from_response(*args, **kwargs): ...
    def new_full(*args, **kwargs): ...
    def new_session_policy(*args, **kwargs): ...
    

class Logger:
    parent = ...
    
    @classmethod
    def new(cls, level: LoggerLogLevel, max_body_size: int) -> Logger: ...
    def set_printer(*args, **kwargs): ...
    def set_request_filter(*args, **kwargs): ...
    def set_response_filter(*args, **kwargs): ...
    

class Message(GObject.Object):
    method = ...
    parent = ...
    reason_phrase = ...
    request_body = ...
    request_headers = ...
    response_body = ...
    response_headers = ...
    status_code: int = ...

    class Props:
        response_headers: Optional[MessageHeaders] = ...
        response_body: Optional[MessageBody] = ...
        response_body_data: Optional[GLib.Bytes] = ...
        uri: Optional[URI] = ...

    props: Props

    def content_sniffed(*args, **kwargs): ...
    def disable_feature(*args, **kwargs): ...
    def finished(*args, **kwargs): ...
    def get_address(*args, **kwargs): ...
    def get_first_party(*args, **kwargs): ...
    def get_flags(*args, **kwargs): ...
    def get_http_version(*args, **kwargs): ...
    def get_https_status(self) -> tuple[bool, Gio.TlsCertificate, Gio.TlsCertificateFlags]: ...
    def get_is_top_level_navigation(*args, **kwargs): ...
    def get_priority(*args, **kwargs): ...
    def get_site_for_cookies(*args, **kwargs): ...
    def get_soup_request(*args, **kwargs): ...
    def get_uri(*args, **kwargs): ...
    def got_body(*args, **kwargs): ...
    def got_chunk(*args, **kwargs): ...
    def got_headers(*args, **kwargs): ...
    def got_informational(*args, **kwargs): ...
    def is_feature_disabled(*args, **kwargs): ...
    def is_keepalive(*args, **kwargs): ...
    @classmethod
    def new(cls, method: str, uri_string: str) -> Message: ...
    def new_from_uri(*args, **kwargs): ...
    def restarted(*args, **kwargs): ...
    def set_chunk_allocator(*args, **kwargs): ...
    def set_first_party(*args, **kwargs): ...
    def set_flags(self, flags: MessageFlags) -> None: ...
    def set_http_version(*args, **kwargs): ...
    def set_is_top_level_navigation(*args, **kwargs): ...
    def set_priority(*args, **kwargs): ...
    def set_redirect(*args, **kwargs): ...
    def set_request(*args, **kwargs): ...
    def set_response(*args, **kwargs): ...
    def set_site_for_cookies(*args, **kwargs): ...
    def set_status(*args, **kwargs): ...
    def set_status_full(*args, **kwargs): ...
    def set_uri(*args, **kwargs): ...
    def starting(*args, **kwargs): ...
    def wrote_body(*args, **kwargs): ...
    def wrote_body_data(*args, **kwargs): ...
    def wrote_chunk(*args, **kwargs): ...
    def wrote_headers(*args, **kwargs): ...
    def wrote_informational(*args, **kwargs): ...
    
    def do_finished(self, *args, **kwargs): ...
    def do_got_body(self, *args, **kwargs): ...
    def do_got_chunk(self, *args, **kwargs): ...
    def do_got_headers(self, *args, **kwargs): ...
    def do_got_informational(self, *args, **kwargs): ...
    def do_restarted(self, *args, **kwargs): ...
    def do_starting(self, *args, **kwargs): ...
    def do_wrote_body(self, *args, **kwargs): ...
    def do_wrote_chunk(self, *args, **kwargs): ...
    def do_wrote_headers(self, *args, **kwargs): ...
    def do_wrote_informational(self, *args, **kwargs): ...
    

class MessageBody:
    data: str = ...
    length: int = ...
    
    def append(*args, **kwargs): ...
    def append_buffer(*args, **kwargs): ...
    def complete(*args, **kwargs): ...
    def flatten(*args, **kwargs): ...
    def free(*args, **kwargs): ...
    def get_accumulate(*args, **kwargs): ...
    def get_chunk(*args, **kwargs): ...
    def got_chunk(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_accumulate(*args, **kwargs): ...
    def truncate(*args, **kwargs): ...
    def wrote_chunk(*args, **kwargs): ...
    

class MessageHeaders:
    def append(*args, **kwargs): ...
    def clean_connection_headers(*args, **kwargs): ...
    def clear(*args, **kwargs): ...
    def foreach(*args, **kwargs): ...
    def free(*args, **kwargs): ...
    def free_ranges(*args, **kwargs): ...
    def get(*args, **kwargs): ...
    def get_content_disposition(*args, **kwargs): ...
    def get_content_length(self) -> int: ...
    def get_content_range(*args, **kwargs): ...
    def get_content_type(*args, **kwargs): ...
    def get_encoding(*args, **kwargs): ...
    def get_expectations(*args, **kwargs): ...
    def get_headers_type(*args, **kwargs): ...
    def get_list(*args, **kwargs): ...
    def get_one(*args, **kwargs): ...
    def get_ranges(*args, **kwargs): ...
    def header_contains(*args, **kwargs): ...
    def header_equals(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def remove(*args, **kwargs): ...
    def replace(*args, **kwargs): ...
    def set_content_disposition(*args, **kwargs): ...
    def set_content_length(*args, **kwargs): ...
    def set_content_range(*args, **kwargs): ...
    def set_content_type(*args, **kwargs): ...
    def set_encoding(*args, **kwargs): ...
    def set_expectations(*args, **kwargs): ...
    def set_range(*args, **kwargs): ...
    def set_ranges(*args, **kwargs): ...
    

class MessageHeadersIter:
    dummy = ...
    
    def init(*args, **kwargs): ...
    def next(*args, **kwargs): ...
    

class MessageQueue: ...

class MessageQueueItem: ...

class Multipart:
    def append_form_file(*args, **kwargs): ...
    def append_form_string(*args, **kwargs): ...
    def append_part(*args, **kwargs): ...
    def free(*args, **kwargs): ...
    def get_length(*args, **kwargs): ...
    def get_part(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_from_message(*args, **kwargs): ...
    def to_message(*args, **kwargs): ...
    

class MultipartInputStream:
    def get_headers(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def next_part(*args, **kwargs): ...
    def next_part_async(*args, **kwargs): ...
    def next_part_finish(*args, **kwargs): ...
    

class PasswordManager:
    def get_passwords_async(*args, **kwargs): ...
    def get_passwords_sync(*args, **kwargs): ...
    

class PasswordManagerInterface:
    base = ...
    get_passwords_async = ...
    get_passwords_sync = ...
    

class ProxyResolver:
    def get_proxy_async(*args, **kwargs): ...
    def get_proxy_sync(*args, **kwargs): ...
    

class ProxyResolverDefault:
    parent = ...
    

class ProxyResolverInterface:
    base = ...
    get_proxy_async = ...
    get_proxy_sync = ...
    

class ProxyURIResolver:
    def get_proxy_uri_async(*args, **kwargs): ...
    def get_proxy_uri_sync(*args, **kwargs): ...
    

class ProxyURIResolverInterface:
    _libsoup_reserved1 = ...
    _libsoup_reserved2 = ...
    _libsoup_reserved3 = ...
    _libsoup_reserved4 = ...
    base = ...
    get_proxy_uri_async = ...
    get_proxy_uri_sync = ...
    

class Range:
    end = ...
    start = ...
    

class Request:
    parent = ...
    priv = ...
    
    def get_content_length(self) -> int: ...
    def get_content_type(self) -> Optional[str]: ...
    def get_session(self) -> Session: ...
    def get_uri(self) -> URI: ...
    def send(*args, **kwargs): ...
    def send_async(*args, **kwargs): ...
    def send_finish(*args, **kwargs): ...
    
    def do_check_uri(self, *args, **kwargs): ...
    def do_get_content_length(self, *args, **kwargs): ...
    def do_get_content_type(self, *args, **kwargs): ...
    def do_send(self, *args, **kwargs): ...
    def do_send_async(self, *args, **kwargs): ...
    def do_send_finish(self, *args, **kwargs): ...
    

class RequestData: ...

class RequestFile:
    def get_file(*args, **kwargs): ...
    

class RequestHTTP:
    def get_message(*args, **kwargs): ...
    

class Requester:
    parent = ...
    priv = ...
    
    def new(*args, **kwargs): ...
    def request(*args, **kwargs): ...
    def request_uri(*args, **kwargs): ...
    

class Server:
    parent = ...
    
    def accept_iostream(*args, **kwargs): ...
    def add_auth_domain(*args, **kwargs): ...
    def add_early_handler(*args, **kwargs): ...
    def add_handler(*args, **kwargs): ...
    def add_websocket_extension(*args, **kwargs): ...
    def add_websocket_handler(*args, **kwargs): ...
    def get_async_context(*args, **kwargs): ...
    def get_listener(*args, **kwargs): ...
    def get_listeners(*args, **kwargs): ...
    def get_port(*args, **kwargs): ...
    def get_uris(*args, **kwargs): ...
    def is_https(*args, **kwargs): ...
    def listen(*args, **kwargs): ...
    def listen_all(*args, **kwargs): ...
    def listen_fd(*args, **kwargs): ...
    def listen_local(*args, **kwargs): ...
    def listen_socket(*args, **kwargs): ...
    def pause_message(*args, **kwargs): ...
    def quit(*args, **kwargs): ...
    def remove_auth_domain(*args, **kwargs): ...
    def remove_handler(*args, **kwargs): ...
    def remove_websocket_extension(*args, **kwargs): ...
    def run(*args, **kwargs): ...
    def run_async(*args, **kwargs): ...
    def set_ssl_cert_file(*args, **kwargs): ...
    def unpause_message(*args, **kwargs): ...
    
    def do_request_aborted(self, *args, **kwargs): ...
    def do_request_finished(self, *args, **kwargs): ...
    def do_request_read(self, *args, **kwargs): ...
    def do_request_started(self, *args, **kwargs): ...


class Session:
    parent = ...

    class Props:
        https_aliases: list[str] = ...
        proxy_resolver: Optional[Gio.ProxyResolver] = ...
        ssl_strict: bool = ...
        user_agent: str = ...

    props = Props
    
    def abort(self) -> None: ...
    def add_feature(self, type: Any) -> bool: ...
    def add_feature_by_type(self, feature_type: GObject.GType) -> None: ...
    def cancel_message(self, msg: Message, status_code: int) -> None: ...
    def connect_async(*args, **kwargs): ...
    def connect_finish(*args, **kwargs): ...
    def get_async_context(*args, **kwargs): ...
    def get_feature(*args, **kwargs): ...
    def get_feature_for_message(*args, **kwargs): ...
    def get_features(*args, **kwargs): ...
    def has_feature(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def pause_message(*args, **kwargs): ...
    def prefetch_dns(*args, **kwargs): ...
    def prepare_for_uri(*args, **kwargs): ...
    @overload
    def queue_message(self, msg: Message, callback: Optional[SessionCallbackU], *user_data: Any) -> None: ...
    @overload
    def queue_message(self, msg: Message, callback: Optional[SessionCallback]) -> None: ...
    def redirect_message(*args, **kwargs): ...
    def remove_feature(*args, **kwargs): ...
    def remove_feature_by_type(*args, **kwargs): ...
    def request(*args, **kwargs): ...
    def request_http(*args, **kwargs): ...
    def request_http_uri(*args, **kwargs): ...
    def request_uri(*args, **kwargs): ...
    def requeue_message(*args, **kwargs): ...
    def send(*args, **kwargs): ...
    def send_async(*args, **kwargs): ...
    def send_finish(*args, **kwargs): ...
    def send_message(*args, **kwargs): ...
    def steal_connection(*args, **kwargs): ...
    def unpause_message(*args, **kwargs): ...
    def websocket_connect_async(self, msg: Message, origin: Optional[str], protocols: Optional[list[str]], cancellable: Optional[Gio.Cancellable], callback: Optional[Gio.AsyncReadyCallback], *user_data: Optional[Any]) -> None: ...
    def websocket_connect_finish(self, result: Gio.AsyncResult) -> WebsocketConnection: ...
    def would_redirect(*args, **kwargs): ...
    
    def do_auth_required(self, *args, **kwargs): ...
    def do_authenticate(self, *args, **kwargs): ...
    def do_cancel_message(self, *args, **kwargs): ...
    def do_flush_queue(self, *args, **kwargs): ...
    def do_kick(self, *args, **kwargs): ...
    def do_queue_message(self, *args, **kwargs): ...
    def do_request_started(self, *args, **kwargs): ...
    def do_requeue_message(self, *args, **kwargs): ...
    def do_send_message(self, *args, **kwargs): ...
    

class SessionAsync: ...

class SessionFeature(GObject.GInterface):
    def add_feature(*args, **kwargs): ...
    def attach(*args, **kwargs): ...
    def detach(*args, **kwargs): ...
    def has_feature(*args, **kwargs): ...
    def remove_feature(*args, **kwargs): ...
    

class SessionFeatureInterface:
    add_feature = ...
    attach = ...
    detach = ...
    has_feature = ...
    parent = ...
    remove_feature = ...
    request_queued = ...
    request_started = ...
    request_unqueued = ...
    

class SessionSync: ...

class Socket:
    parent = ...
    
    def connect_async(*args, **kwargs): ...
    def connect_sync(*args, **kwargs): ...
    def get_fd(*args, **kwargs): ...
    def get_local_address(*args, **kwargs): ...
    def get_remote_address(*args, **kwargs): ...
    def is_connected(*args, **kwargs): ...
    def is_ssl(*args, **kwargs): ...
    def listen(*args, **kwargs): ...
    def read(*args, **kwargs): ...
    def read_until(*args, **kwargs): ...
    def start_proxy_ssl(*args, **kwargs): ...
    def start_ssl(*args, **kwargs): ...
    def write(*args, **kwargs): ...
    
    def do_disconnected(self, *args, **kwargs): ...
    def do_new_connection(self, *args, **kwargs): ...
    def do_readable(self, *args, **kwargs): ...
    def do_writable(self, *args, **kwargs): ...
    

class URI:
    fragment = ...
    host = ...
    password = ...
    path = ...
    port = ...
    query = ...
    scheme = ...
    user = ...
    
    def copy_host(*args, **kwargs): ...
    def decode(*args, **kwargs): ...
    def encode(*args, **kwargs): ...
    def equal(*args, **kwargs): ...
    def free(*args, **kwargs): ...
    def get_fragment(*args, **kwargs): ...
    def get_host(*args, **kwargs): ...
    def get_password(*args, **kwargs): ...
    def get_path(*args, **kwargs): ...
    def get_port(*args, **kwargs): ...
    def get_query(*args, **kwargs): ...
    def get_scheme(*args, **kwargs): ...
    def get_user(*args, **kwargs): ...
    def host_equal(*args, **kwargs): ...
    def host_hash(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_with_base(*args, **kwargs): ...
    def normalize(*args, **kwargs): ...
    def set_fragment(*args, **kwargs): ...
    def set_host(*args, **kwargs): ...
    def set_password(*args, **kwargs): ...
    def set_path(*args, **kwargs): ...
    def set_port(*args, **kwargs): ...
    def set_query(*args, **kwargs): ...
    def set_query_from_form(*args, **kwargs): ...
    def set_scheme(*args, **kwargs): ...
    def set_user(*args, **kwargs): ...
    def to_string(self, just_path_and_query: bool) -> str: ...
    def uses_default_port(*args, **kwargs): ...
    

class WebsocketConnection(GObject.Object):
    parent = ...
    pv = ...
    
    def close(self, code: WebsocketCloseCode, data: Optional[bytes]) -> None: ...
    def get_close_code(*args, **kwargs): ...
    def get_close_data(*args, **kwargs): ...
    def get_connection_type(*args, **kwargs): ...
    def get_extensions(*args, **kwargs): ...
    def get_io_stream(*args, **kwargs): ...
    def get_keepalive_interval(*args, **kwargs): ...
    def get_max_incoming_payload_size(*args, **kwargs): ...
    def get_origin(*args, **kwargs): ...
    def get_protocol(*args, **kwargs): ...
    def get_state(*args, **kwargs): ...
    def get_uri(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_with_extensions(*args, **kwargs): ...
    def send_binary(self, data: Optional[bytes]) -> None: ...
    def send_message(*args, **kwargs): ...
    def send_text(*args, **kwargs): ...
    def set_keepalive_interval(self, interval: int) -> None: ...
    def set_max_incoming_payload_size(*args, **kwargs): ...
    
    def do_closed(self, *args, **kwargs): ...
    def do_closing(self, *args, **kwargs): ...
    def do_error(self, *args, **kwargs): ...
    def do_message(self, *args, **kwargs): ...
    def do_pong(self, *args, **kwargs): ...
    

class WebsocketExtension:
    parent = ...
    
    def configure(*args, **kwargs): ...
    def get_request_params(*args, **kwargs): ...
    def get_response_params(*args, **kwargs): ...
    def process_incoming_message(*args, **kwargs): ...
    def process_outgoing_message(*args, **kwargs): ...
    
    def do_configure(self, *args, **kwargs): ...
    def do_get_request_params(self, *args, **kwargs): ...
    def do_get_response_params(self, *args, **kwargs): ...
    def do_process_incoming_message(self, *args, **kwargs): ...
    def do_process_outgoing_message(self, *args, **kwargs): ...
    

class WebsocketExtensionDeflate: ...

class WebsocketExtensionManager:
    parent = ...
    

class XMLRPCParams:
    def free(*args, **kwargs): ...
    def parse(*args, **kwargs): ...
    

class Cacheability(GObject.GFlags):
    CACHEABLE = ...
    UNCACHEABLE = ...
    INVALIDATES = ...
    VALIDATES = ...

class Expectation(GObject.GFlags):
    UNRECOGNIZED = ...
    CONTINUE = ...

class MessageFlags(GObject.GFlags):
    NO_REDIRECT = ...
    CAN_REBUILD = ...
    OVERWRITE_CHUNKS = ...
    CONTENT_DECODED = ...
    CERTIFICATE_TRUSTED = ...
    NEW_CONNECTION = ...
    IDEMPOTENT = ...
    IGNORE_CONNECTION_LIMITS = ...
    DO_NOT_USE_AUTH_CACHE = ...

class ServerListenOptions(GObject.GFlags):
    HTTPS = ...
    IPV4_ONLY = ...
    IPV6_ONLY = ...

class AddressFamily(GObject.GEnum):
    INVALID = ...
    IPV4 = ...
    IPV6 = ...

class CacheResponse(GObject.GEnum):
    FRESH = ...
    NEEDS_VALIDATION = ...
    STALE = ...

class CacheType(GObject.GEnum):
    SINGLE_USER = ...
    SHARED = ...

class ConnectionState(GObject.GEnum):
    NEW = ...
    CONNECTING = ...
    IDLE = ...
    IN_USE = ...
    REMOTE_DISCONNECTED = ...
    DISCONNECTED = ...

class CookieJarAcceptPolicy(GObject.GEnum):
    ALWAYS = ...
    NEVER = ...
    NO_THIRD_PARTY = ...
    GRANDFATHERED_THIRD_PARTY = ...

class DateFormat(GObject.GEnum):
    HTTP = ...
    COOKIE = ...
    RFC2822 = ...
    ISO8601_COMPACT = ...
    ISO8601_FULL = ...
    ISO8601 = ...
    ISO8601_XMLRPC = ...

class Encoding(GObject.GEnum):
    UNRECOGNIZED = ...
    NONE = ...
    CONTENT_LENGTH = ...
    EOF = ...
    CHUNKED = ...
    BYTERANGES = ...

class HTTPVersion(GObject.GEnum):
    HTTP_1_0 = ...
    HTTP_1_1 = ...

class KnownStatusCode(GObject.GEnum):
    NONE = ...
    CANCELLED = ...
    CANT_RESOLVE = ...
    CANT_RESOLVE_PROXY = ...
    CANT_CONNECT = ...
    CANT_CONNECT_PROXY = ...
    SSL_FAILED = ...
    IO_ERROR = ...
    MALFORMED = ...
    TRY_AGAIN = ...
    TOO_MANY_REDIRECTS = ...
    TLS_FAILED = ...
    CONTINUE = ...
    SWITCHING_PROTOCOLS = ...
    PROCESSING = ...
    OK = ...
    CREATED = ...
    ACCEPTED = ...
    NON_AUTHORITATIVE = ...
    NO_CONTENT = ...
    RESET_CONTENT = ...
    PARTIAL_CONTENT = ...
    MULTI_STATUS = ...
    MULTIPLE_CHOICES = ...
    MOVED_PERMANENTLY = ...
    FOUND = ...
    MOVED_TEMPORARILY = ...
    SEE_OTHER = ...
    NOT_MODIFIED = ...
    USE_PROXY = ...
    NOT_APPEARING_IN_THIS_PROTOCOL = ...
    TEMPORARY_REDIRECT = ...
    BAD_REQUEST = ...
    UNAUTHORIZED = ...
    PAYMENT_REQUIRED = ...
    FORBIDDEN = ...
    NOT_FOUND = ...
    METHOD_NOT_ALLOWED = ...
    NOT_ACCEPTABLE = ...
    PROXY_AUTHENTICATION_REQUIRED = ...
    PROXY_UNAUTHORIZED = ...
    REQUEST_TIMEOUT = ...
    CONFLICT = ...
    GONE = ...
    LENGTH_REQUIRED = ...
    PRECONDITION_FAILED = ...
    REQUEST_ENTITY_TOO_LARGE = ...
    REQUEST_URI_TOO_LONG = ...
    UNSUPPORTED_MEDIA_TYPE = ...
    REQUESTED_RANGE_NOT_SATISFIABLE = ...
    INVALID_RANGE = ...
    EXPECTATION_FAILED = ...
    UNPROCESSABLE_ENTITY = ...
    LOCKED = ...
    FAILED_DEPENDENCY = ...
    INTERNAL_SERVER_ERROR = ...
    NOT_IMPLEMENTED = ...
    BAD_GATEWAY = ...
    SERVICE_UNAVAILABLE = ...
    GATEWAY_TIMEOUT = ...
    HTTP_VERSION_NOT_SUPPORTED = ...
    INSUFFICIENT_STORAGE = ...
    NOT_EXTENDED = ...

class LoggerLogLevel(GObject.GEnum):
    NONE = ...
    MINIMAL = ...
    HEADERS = ...
    BODY = ...

class MemoryUse(GObject.GEnum):
    STATIC = ...
    TAKE = ...
    COPY = ...
    TEMPORARY = ...

class MessageHeadersType(GObject.GEnum):
    REQUEST = ...
    RESPONSE = ...
    MULTIPART = ...

class MessagePriority(GObject.GEnum):
    VERY_LOW = ...
    LOW = ...
    NORMAL = ...
    HIGH = ...
    VERY_HIGH = ...

class RequestError(GObject.GEnum):
    BAD_URI = ...
    UNSUPPORTED_URI_SCHEME = ...
    PARSING = ...
    ENCODING = ...
    quark = ...

class RequesterError(GObject.GEnum):
    BAD_URI = ...
    UNSUPPORTED_URI_SCHEME = ...
    quark = ...

class SameSitePolicy(GObject.GEnum):
    NONE = ...
    LAX = ...
    STRICT = ...

class SocketIOStatus(GObject.GEnum):
    OK = ...
    WOULD_BLOCK = ...
    EOF = ...
    ERROR = ...

class Status(GObject.GEnum):
    NONE = ...
    CANCELLED = ...
    CANT_RESOLVE = ...
    CANT_RESOLVE_PROXY = ...
    CANT_CONNECT = ...
    CANT_CONNECT_PROXY = ...
    SSL_FAILED = ...
    IO_ERROR = ...
    MALFORMED = ...
    TRY_AGAIN = ...
    TOO_MANY_REDIRECTS = ...
    TLS_FAILED = ...
    CONTINUE = ...
    SWITCHING_PROTOCOLS = ...
    PROCESSING = ...
    OK = ...
    CREATED = ...
    ACCEPTED = ...
    NON_AUTHORITATIVE = ...
    NO_CONTENT = ...
    RESET_CONTENT = ...
    PARTIAL_CONTENT = ...
    MULTI_STATUS = ...
    MULTIPLE_CHOICES = ...
    MOVED_PERMANENTLY = ...
    FOUND = ...
    MOVED_TEMPORARILY = ...
    SEE_OTHER = ...
    NOT_MODIFIED = ...
    USE_PROXY = ...
    NOT_APPEARING_IN_THIS_PROTOCOL = ...
    TEMPORARY_REDIRECT = ...
    PERMANENT_REDIRECT = ...
    BAD_REQUEST = ...
    UNAUTHORIZED = ...
    PAYMENT_REQUIRED = ...
    FORBIDDEN = ...
    NOT_FOUND = ...
    METHOD_NOT_ALLOWED = ...
    NOT_ACCEPTABLE = ...
    PROXY_AUTHENTICATION_REQUIRED = ...
    PROXY_UNAUTHORIZED = ...
    REQUEST_TIMEOUT = ...
    CONFLICT = ...
    GONE = ...
    LENGTH_REQUIRED = ...
    PRECONDITION_FAILED = ...
    REQUEST_ENTITY_TOO_LARGE = ...
    REQUEST_URI_TOO_LONG = ...
    UNSUPPORTED_MEDIA_TYPE = ...
    REQUESTED_RANGE_NOT_SATISFIABLE = ...
    INVALID_RANGE = ...
    EXPECTATION_FAILED = ...
    UNPROCESSABLE_ENTITY = ...
    LOCKED = ...
    FAILED_DEPENDENCY = ...
    INTERNAL_SERVER_ERROR = ...
    NOT_IMPLEMENTED = ...
    BAD_GATEWAY = ...
    SERVICE_UNAVAILABLE = ...
    GATEWAY_TIMEOUT = ...
    HTTP_VERSION_NOT_SUPPORTED = ...
    INSUFFICIENT_STORAGE = ...
    NOT_EXTENDED = ...
    get_phrase = ...
    proxify = ...

class TLDError(GObject.GEnum):
    INVALID_HOSTNAME = ...
    IS_IP_ADDRESS = ...
    NOT_ENOUGH_DOMAINS = ...
    NO_BASE_DOMAIN = ...
    NO_PSL_DATA = ...
    quark = ...

class WebsocketCloseCode(GObject.GEnum):
    NORMAL = ...
    GOING_AWAY = ...
    PROTOCOL_ERROR = ...
    UNSUPPORTED_DATA = ...
    NO_STATUS = ...
    ABNORMAL = ...
    BAD_DATA = ...
    POLICY_VIOLATION = ...
    TOO_BIG = ...
    NO_EXTENSION = ...
    SERVER_ERROR = ...
    TLS_HANDSHAKE = ...

class WebsocketConnectionType(GObject.GEnum):
    UNKNOWN = ...
    CLIENT = ...
    SERVER = ...

class WebsocketDataType(GObject.GEnum):
    TEXT = ...
    BINARY = ...

class WebsocketError(GObject.GEnum):
    FAILED = ...
    NOT_WEBSOCKET = ...
    BAD_HANDSHAKE = ...
    BAD_ORIGIN = ...
    get_quark = ...

class WebsocketState(GObject.GEnum):
    OPEN = ...
    CLOSING = ...
    CLOSED = ...

class XMLRPCError(GObject.GEnum):
    ARGUMENTS = ...
    RETVAL = ...
    quark = ...

class XMLRPCFault(GObject.GEnum):
    PARSE_ERROR_NOT_WELL_FORMED = ...
    PARSE_ERROR_UNSUPPORTED_ENCODING = ...
    PARSE_ERROR_INVALID_CHARACTER_FOR_ENCODING = ...
    SERVER_ERROR_INVALID_XML_RPC = ...
    SERVER_ERROR_REQUESTED_METHOD_NOT_FOUND = ...
    SERVER_ERROR_INVALID_METHOD_PARAMETERS = ...
    SERVER_ERROR_INTERNAL_XML_RPC_ERROR = ...
    APPLICATION_ERROR = ...
    SYSTEM_ERROR = ...
    TRANSPORT_ERROR = ...
    quark = ...
