def add_application(graph, trace):
    """A software application."""


# id (string) - The unique identifier of the application.
# installedOn (date) - The installation date of the application.
# misc (map:string) - Additional information about the application.
# name (string) - The name of the application.
# package (string) - The package of the application, e.g. com.example.ExampleMessenger.
# permissions (list:string) - The permissions requested by the application.
# purchasedOn (date) - The purchase date of the application.
# version (string) - The registered version of the application.


def add_applicationArchive(graph, trace):
    """A list of applications."""


# misc (map:string) - Additional information about the application archive.


def add_attachment(graph, trace):
    """An attached block of data."""


# application (string) - The name of the application from which the attachment originates.
# encoding (string) - The encoding that is used for sending the attachment, e.g. BASE64, BITS_7.
# misc (map:string) - Additional information about the attachment.
# name (string) - The name of the attachment.
# type (string) - The type of attachment.


def add_audio(graph, trace):
    """A media trace that contains audio."""


# bitrate (integer) - The bitrate of the audio in bits per second.
# duration (integer) - The duration of the audio in seconds.
# format (string) - The format of the audio. For example: mp3 or flac.
# metadata (map:string) - Audio metadata, e.g. title, genre, artist.
# misc (map:string) - Additional information about the audio.


def add_bookmark(graph, trace):
    """A bookmark to a web pages or files using a web browser."""


# accessedOn (date) - The date and time at which the web page or file was last opened.
# application (string) - The name of the web browser from which the bookmarks originates.
# createdOn (date) - The date and time at which this bookmark was created.
# misc (map:string) - Additional information about the bookmark.
# modifiedOn (date) - The date and time at which this bookmark was last modified.
# name (string) - The name of the bookmark.
# path (string) - The folder containing the bookmark.
# url (string) - The target of the bookmark.
# visitCount (integer) - The minimal number of times this bookmark has been visited by this web browser.


def add_bookmarkArchive(graph, trace):
    """A list of bookmarks to web pages and files using a web browser."""


# application (string) - The name of the web browser from which the bookmarks originates.
# misc (map:string) - Additional information about the bookmarkArchive.


def add_browserHistory(graph, trace):
    """Information on a web page or file that has been visited with a web browser."""


# accessedOn (date) - The date and time at which the web page or file was last visited.
# application (string) - The name of the web browser that was used to visit the web page or file.
# createdOn (date) - The date and time at which this log entry was created.
# misc (map:string) - Additional information on this browser history.
# modifiedOn (date) - The date and time at which this visited web page or file was last modified. This timestamp is provided by the web site's server.
# pageTitle (string) - The title of the visited web page or file.
# type (string) - The type of page or file that has been visited, typically this property has value "URL".
# url (string) - The address of the visited web page or file.
# user (string) - The user that visited this web page or file.
# visitCount (integer) - The minimal number of times this web page or file has been visited by this web browser.


def add_browserHistoryLog(graph, trace):
    """Log containing the history of visited web pages and files with a web browser."""


# application (string) - The name of the web browser from which the log originates.
# misc (map:string) - Additional information about the browserHistoryLog.


def add_calendar(graph, trace):
    """A collection of appointments and meetings."""


# application (string) - The application for which this a calendar.
# misc (map:string) - Additional information about the calendar.
# owner (string) - The owner of the calendar.


def add_calendarEntry(graph, trace):
    """An entry in a calendar, for instance an appointment or a meeting."""


# application (string) - The application for which this a calendar entry.
# attendees (list:string) - The attendees of the event.
# categories (list:string) - Categories applied to the event.
# createdOn (date) - The date and time at which the calendar entry was created.
# duration (integer) - The duration of the event.
# endsOn (date) - The date and time at which the event ends.
# importance (string) - The importance of the calendar entry.
# labels (map:string) - Named and colored label.
# location (string) - The location of the event.
# misc (map:string) - Additional information on the calendar entry.
# modifiedOn (date) - The date and time at which the calendar entry was last modified.
# owner (string) - The organizer of the calendar event.
# private (boolean) - Is the event marked as private?
# recurrence (string) - Recurrence of the event.
# remindOn (date) - The date and time at which a reminder is given about the calendar entry.
# startsOn (date) - The date and time at which the event starts.
# status (string) - The status of the event, for instance accepted, pending or cancelled.
# subject (string) - The subject of the event.
# timestamps (map:date) - Additional timestamps for an event.
# type (string) - A free format text identifier, used for identifying type of calendar entry, for instance meeting or event.


def add_carved(graph, trace):
    """A carved trace is not available in the file system, but is found in the (unallocated) binary data in the image."""


# partial (boolean) - Partial is set to true if the carved trace is only partially recovered.


def add_certificate(graph, trace):
    """A certificate."""


# beginsOn (date) - The certificate is not valid before this date.
# expiresOn (date) - The certificate is not valid after this date.
# issuer (string) - The issuer of the certificate.
# misc (map:string) - Additional information.
# serialNumber (string) - The serial number of the certificate.
# subject (string) - The subject of the certificate.
# version (string) - The version of the certificate.


def add_chatConversation(graph, trace):
    """A set of messages from one chat conversation."""


# administrators (list:string) - A list of administrators in this chat conversation.
# application (string) - The application for which this is a chat conversation, e.g. "Skype" or "MSN".
# createdOn (date) - The date and time at which the conversation was created.
# misc (map:string) - Additional information about the chat conversation.
# participants (list:string) - A list of members in this chat conversation.
# subject (string) - The subject of the chat conversation.


def add_chatEvent(graph, trace):
    """Log containing a chat event, e.g. the transfer of a file or the opening of a webcam session."""


# application (string) - The application for which this is a log file, e.g. "Skype" or "MSN".
# from (string) - The sending user.
# message (string) - Message attached to the event.
# messageId (string) - An identifier for the chat event.
# misc (map:string) - Additional information about the chat event.
# sentOn (date) - The time at which the chat entry was sent.
# sessionId (string) - An identifier for the chat session in which the chat log entry took place.
# timestamps (map:date) - Additional timestamps for the chat event.
# to (list:string) - The receiving users.
# type (string) - The type of chat log entry, e.g. invitation, join, leave.


def add_chatLog(graph, trace):
    """Log containing chat history."""


# application (string) - The application for which this is a log file, e.g. "Skype" or "MSN".
# misc (map:string) - Additional information about the chatLog.


def add_chatMessage(graph, trace):
    """A single message sent in a chat."""


# application (string) - The application for which this is a chat message, e.g. "Skype" or "MSN".
# deliveredOn (date) - The time at which the chat message was delivered.
# from (string) - The sending user.
# message (string) - The contents of the message.
# messageId (string) - An identifier for the chat message.
# misc (map:string) - Additional information about the chat message.
# readOn (date) - The time at which the chat message was read.
# sentOn (date) - The time at which the chat message was sent.
# sessionId (string) - An identifier for the chat session from which the chat message originates.
# timestamps (map:date) - Additional timestamps for the chat message.
# to (list:string) - The receiving users.


def add_compressed(graph, trace):
    """Compressed data, e.g. zip"""


# algorithm (string) - The algorithm used to compress the trace.
# compressedSize (integer) - The number of bytes of the compressed data.
# compressionRatio (real) - The compression ratio of the compressed data.
# misc (map:string) - Additional information about the compression.
# modifiedOn (date) - The last time the compressed content was changed.
# originalName (string) - The name of the original file.
# originalOperatingSystem (string) - The original operating system that created the file.


def add_connection(graph, trace):
    """Connection to a network."""


# accessedOn (date) - The time the connection was last accessed.
# baseStation (string) - The base station.
# createdOn (date) - The time the connection was initiated for the first time.
# description (string) - Description.
# encryptionKey (string) - The encryption key.
# expiresOn (date) - The time the connection is going to expire.
# misc (map:string) - Additional information on the connection.
# ssid (string) - Network identifier.
# timestamps (map:date) - Additional timestamps for the connection.
# type (string) - The type of the connection.


def add_connectionArchive(graph, trace):
    """A list of connections."""


# misc (map:string) - Additional information about the connection archive.


def add_cookie(graph, trace):
    """A piece of data used by a (remote) web page, stored on the local machine."""


# accessedOn (date) - The last time at which the cookie was accessed.
# application (string) - The name/identifier of the web browser from which cookies is extracted.
# createdOn (date) - The date and time at which the cookie was created.
# domain (string) - The domain for which the cookie is stored, for example nfi.minjus.nl.
# expiresOn (date) - The expiration time of the cookie.
# misc (map:string) - Additional information about the cookie.
# name (string) - The name of the cookie.
# path (string) - String representation of the path of the cookie.
# secure (boolean) - If the cookie is secure it cannot be delivered over an unencrypted session such as http.


def add_cookieArchive(graph, trace):
    """A collection of cookies."""


# application (string) - The application for which this trace is a cookieArchive for example FireFox or IE.
# misc (map:string) - Additional information about the cookieArchive.


def add_cryptoKey(graph, trace):
    """A encryption/decryption key."""


# algorithm (string) - The algorithm for which the key is used.
# base64 (string) - The contents of the key represented as base64.
# createdOn (date) - The date this key is created.
# encoded (binary) - The contents of the key encoded in the given format.
# format (string) - The format used to encode the key.
# hasPrivate (boolean) - Whether the key contains a private key.
# isMaster (boolean) - Whether the key is a master key.
# misc (map:string) - Additional information.
# serialNumber (string) - The id of the key.
# type (string) - The type of key, for example private, public or secret.
# userIds (list:string) - The user IDs associated with the key.


def add_cryptoKeyPair(graph, trace):
    """Two crypto keys of types public and private."""


# application (string) - The name of the application used for this key pair.
# misc (map:string) - Additional information about the cryptoKeyPair.


def add_cryptocurrencyWallet(graph, trace):
    """A collection of crypto keys and contacts of a cryptocurrency wallet."""


# misc (map:string) - Additional information about the attachment.
# type (string) - The type of the cryptocurrency wallet, for example Bitcoin, Litecoin or Ethereum.


def add_data(graph, trace):
    """The data (content) of the trace, indexed by data type. For example data.raw.size, data.text.size"""


# descriptor (binary) - An opaque reference to the actual bytes that make up the data.
# entropy (real) - Shannon entropy (a measure of randomness) of the data.
# fileType (string) - File type of the data. For example 'Adobe Pdf'.
# hash (map:string) - Hash values of the data, keyed by algorithm. For example: hash.md5='d41d8cd98f00b204e9800998ecf8427e', hash.sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709'
# hashHitInfo (map:string) - Information about a hash hit. For example: hashHitInfo.nsrl.os='Windows'
# hashHits (list:string) - A list of hash sets that contain a hash of this trace.
# hashMisses (list:string) - A list of hash sets that do NOT contain a hash of this trace.
# imageOffset (integer) - The offset at which the start of data can be found, relative to the start of the image data.
# mimeClass (string) - MIME type derived classification of the data. For example 'audio', 'document', 'picture', or 'text'.
# mimeType (string) - MIME type of the data. For example 'text/html' or 'audio/mp3'.
# parentOffset (integer) - The offset at which the start of data can be found, relative to the start of the parent trace's data.
# size (integer) - The size of the data in bytes.
# type (string) - The type of data, contains the key: raw, text, plain...


def add_deleted(graph, trace):
    """A trace that has been deleted from the file system, or has been placed in a recycle bin or trash can."""


# deletedOn (date) - The deletion time of the trace.
# misc (map:string) - Additional information about the deleted trace.
# originalName (string) - The name of the trace before it was deleted.
# originalPath (string) - The path of the trace before it was deleted.
# originalSize (integer) - The size of the trace before it was deleted.


def add_dns(graph, trace):
    """IP DNS information regardless of lookup or reverselookup"""


# ip (string) - An ip address in dotted notation or semicolon notation for IPv6.
# misc (map:string) - Additional information about the DNS information.


def add_document(graph, trace):
    """A document, for example an Office documents."""


# application (string) - The name of the application used to author the file.
# author (string) - The author of the document.
# createdOn (date) - The date and time at which the document was created.
# lastAuthor (string) - The last author that updated the document.
# lastPrintedOn (date) - The time at which the document was last printed.
# lastSavedOn (date) - The time at which the document was last saved.
# misc (map:string) - Additional information about the document, e.g. keywords, comments and revisions.
# pageCount (integer) - The number of pages in the document.
# subject (string) - The subject of the document.
# title (string) - The title of the document.
# type (string) - The type of the document, e.g. document, spreadsheet or presentation.


def add_email(graph, trace):
    """An electronically sent mail message."""


# application (string) - The application storing this email.
# bcc (list:string) - A list of blank carbon copied receiver's email addresses.
# categories (map:string) - Categories applied to the email.
# cc (list:string) - A list of carbon copied receiver's email addresses.
# createdOn (date) - The date and time at which the email was created.
# from (string) - The sender's email address.
# hasAttachment (boolean) - Indicates if the email has an attachment.
# headers (map:string) - The email headers of the email.
# inReplyTo (string) - A unique identifier for identifying the email this email is a reply to.
# labels (map:string) - Named and colored label.
# messageId (string) - A unique identifier for identifying the email.
# misc (map:string) - Additional information about the email.
# modifiedOn (date) - The time at which the email and/or its read status was last modified.
# priority (string) - The priority of the email.
# read (boolean) - Indicates if the email has been marked as read.
# receivedOn (date) - The time at which the email message was received.
# references (list:string) - A list of email message identifiers this email relates to.
# sentOn (date) - The time at which the email was sent.
# subject (string) - The subject of the email.
# to (list:string) - A lists of receiver's email addresses.


def add_emailArchive(graph, trace):
    """An archive containing email folders and/or messages."""


# application (string) - The application using this emailArchive.
# misc (map:string) - Additional information about the email archive.
# name (string) - The name of the email archive.


def add_emailFolder(graph, trace):
    """A folder containing email messages."""


# application (string) - The application storing this email folder.
# messageCount (integer) - The number of email messages in the email folder.
# misc (map:string) - Additional information about the email folder.
# name (string) - The name of the email folder.
# unreadMessageCount (integer) - The number of unread email messages in the email folder.


def add_encrypted(graph, trace):
    """Data is recognized to be encrypted and can only be viewed with a cryptoKey or password."""


# algorithm (string) - The algorithm used to encrypt the trace.
# application (string) - The name of the application used to encrypt the trace.
# decrypted (boolean) - Whether the encrypted trace is decrypted.
# decryptionKey (string) - A string representation of the key used to decrypt this trace, base64 encoded if needed.
# decryptionKeySerialNumber (string) - The serial number of the key used to decrypt this trace.
# decryptionKeySerialNumbers (list:string) - All serial numbers of the certificates of the keys that can decrypt this trace.
# description (string) - Describes the encrypted trace.
# misc (map:string) - Additional information about the encrypted trace.


def add_event(graph, trace):
    """An event, mainly used for operating system events."""


# action (string) - The action taken in response to the event.
# application (string) - The application that generated the event.
# category (string) - The category of the event, a number or text to classify the event.
# computerName (string) - A name of the computer on which the log entry was created.
# createdOn (date) - The date and time at which the event was created.
# generatedOn (date) - The time at which the event was generated.
# id (string) - The identifier of the event.
# index (integer) - The index of the event in the event log.
# misc (map:string) - Additional information on the event log entry.
# source (string) - The source of the event, for example the name of the application that caused the event to occur.
# startedOn (date) - The time at which the event started.
# text (string) - The textual representation of the event.
# type (string) - The type of the event, for example "information", "warning" or "error".
# user (string) - The user for whom the event was created.


def add_eventLog(graph, trace):
    """Log containing events, amongst others from the operating system."""


# application (string) - The application for which this is an event log.
# misc (map:string) - Additional information on the event log.


def add_executable(graph, trace):
    """An executable or dll file."""


# application (string) - The name of the application used to author the file.
# architecture (string) - The architecture of the system this executable was compiled for.
# compiledOn (date) - The date and time at which the executable was compiled.
# majorVersion (integer) - The major version of this executable.
# minorVersion (integer) - The minor version of this executable.
# misc (map:string) - Additional information.
# subSystem (string) - The subsystem the executable is built for.


def add_fileTransfer(graph, trace):
    """A file transfer log entry contains the details of a file transfer that took place."""


# application (string) - The application used for the file transfer., e.g. "FTP" or "MSN".
# destinationPath (string) - The destination for the file that is transferred.
# finishedOn (date) - The time at which the file transfer finished.
# from (string) - The sending user.
# fromHost (string) - The source address of the file transfer.
# message (string) - Additional message attached to the file transfer.
# messageId (string) - An identifier for the file transfer.
# misc (map:string) - Additional information on the file transfer.
# sessionId (string) - An identifier for the session in which the file transfer took place.
# source (string) - The source of the file that is transferred.
# startedOn (date) - The time at which the file transfer started.
# timestamps (map:date) - Additional timestamps for the file transfer.
# to (list:string) - The receiving users.
# toHosts (list:string) - The destination addresses of the file transfer.
# transferredOn (date) - The time at which the file transfer took place (used when no explicit start and finished time is available).
# type (string) - The direction of the file transfer, e.g. send or receive.


def add_fileTransferLog(graph, trace):
    """A file transfer log contains the history of a file transfers."""


# application (string) - The application used for the file transfer., e.g. "FTP" or "MSN".
# misc (map:string) - Additional information about the file transfer.


def add_gps(graph, trace):
    """A GPS location, a possibly timed global position."""


# application (string) - The application which stores the GPS entry.
# createdOn (date) - The date and time at which the GPS entry was created.
# hdop (real) - The horizontal dilution of precision of the GPS location.
# latlong (latLong) - The latitude and longitude of the GPS location in decimal degrees.
# misc (map:string) - Additional information about the GPS location.
# pdop (real) - The positional (3D) dilution of precision of the GPS location.
# tdop (real) - The temporal dilution of precision of the GPS location.
# vdop (real) - The vertical dilution of precision of the GPS location.


def add_gpsLog(graph, trace):
    """A log containing tracks and/or gps entries."""


# application (string) - The application for which this is a log file, e.g. "Tom Tom Go 6100".
# createdOn (date) - The date/time this gpsLog was created.
# description (string) - A free text description of the gpsLog.
# misc (map:string) - Additional information about the gpsLog.
# name (string) - The name of the gpsLog.


def add_identity(graph, trace):
    """An identity is a small contact card that describes identifiers used elsewhere in the trace."""


# emailAddress (string) - The email address of the identity.
# firstName (string) - The first name of the identity.
# id (string) - The unique identifier of the identity, for example an email address, username or phone number.
# lastName (string) - The last name of the identity.
# ldapDn (string) - The ldap distinguished names of the identity.
# name (string) - The name of the identity.
# originalValue (string) - The original value from which identity properties were extracted, e.g. "John Doe <john@doe.com>".
# phoneNumber (string) - The phone number of the identity.
# screenName (string) - The display name of the identity.
# status (string) - The social status of the identity , e.g. "being happy", "at the gym", ... .
# username (string) - The username of the identity.
# uuid (string) - The universal unique id of the identity.


def add_image(graph, trace):
    """An image is an artifact, that has a similar appearance to some subject - usually a physical object."""


# description (string) - A free text description of the image.
# misc (map:string) - Additional information about the image.
# name (string) - The name of the image.
# type (string) - The type of the image, e.g. EnCase, RAW or LocalFolder.


def add_intercept(graph, trace):
    """The result of a lawful intercept warrant"""


# imei (string) - The International Mobile Station Equipment Identity (IMEI) of the device involved in the intercept.
# imsi (string) - The International Mobile Subscriber Identity (IMSI) of the Subscriber Identity Module (SIM) card involved in the intercept.
# misc (map:string) - Additional information about the intercept.
# msisdn (string) - The telephone number of the subscriber (MSISDN : Mobile Station International Subscriber Directory Number) involved in the intercept.
# type (string) - The original type of intercept used.


def add_interceptLocation(graph, trace):
    """All location related information."""


# azimuth (real) - Orientation of the main antenna beam
# ecgi (string) - The 'E-UTRAN Cell Global Identity' (E-CGI). This parameter is only applicable to the CS traffic cases where the available location information is the one received from the Mobility Management Entity (MME).
# globalCellId (string) - The global cell id.
# misc (map:string) - Additional information about the intercept location.
# observedOn (date) - The date/time this location was observed.
# rai (string) - The Routeing Area Identifier (RAI) in the current Serving GPRS Support Node (SGSN).
# tai (string) - The Tracking Area Identity. This parameter is only applicable to the CS traffic where the available location information is the one received from the Mobility Management Entity (MME).


def add_ipSession(graph, trace):
    """IP Transport layer information"""


# destinationIp (string) - The destination ip address in dotted notation or semicolon notation for IPv6.
# destinationPort (integer) - The destination port for a UDP or TCP connection.
# ipProtocol (string) - IP protocol by name like tcp, udp or number for unknown protocols.
# misc (map:string) - Additional information about the ipSession.
# sourceIp (string) - The source ip address in dotted notation or semicolon notation for IPv6.
# sourcePort (integer) - The source port for a UDP or TCP connection.


def add_link(graph, trace):
    """A link (or shortcut) is a trace that links to another trace."""


# accessedOn (date) - The last time at which the link (shortcut) was accessed.
# arguments (string) - The arguments that are passed to the trace that is linked.
# createdOn (date) - The date and time at which the link was created.
# description (string) - A free text description of the link.
# misc (map:string) - Additional information on the link.
# modifiedOn (date) - The time at which the link was last modified.
# target (string) - The URI, file or folder that is linked.
# targetFileLength (integer) - The length of the trace that is linked.
# timestamps (map:date) - Additional timestamps found for links.
# type (string) - The type of the link.
# volumeLabel (string) - The label of the volume that is linked to.
# volumeSerial (string) - The serial number of the volume that is linked to.
# volumeType (string) - The type of the volume that is linked to.
# workingDirectory (string) - The name of the directory in which the target of the link must be executed.


def add_memory(graph, trace):
    """A piece of data in memory."""


# address (string) - The address in memory of the trace.
# misc (map:string) - Additional information about the memory trace.


def add_memoryImage(graph, trace):
    """An image of a memory dump."""


# createdOn (date) - The date and time at which the memory image was created.
# misc (map:string) - Additional information about the memoryImage.
# name (string) - The name of the memory trace.
# physicalAddressExtension (boolean) - Indicates if the memory image uses physical address extension (PAE).


def add_note(graph, trace):
    """An note."""


# application (string) - The application storing the note.
# categories (map:string) - Categories applied to the note.
# content (string) - The content of the note.
# createdOn (date) - The date and time at which the note was created.
# labels (map:string) - Label applied to the note.
# misc (map:string) - Additional information about the note.
# modifiedOn (date) - The date and time at which the note was last modified.


def add_noteArchive(graph, trace):
    """A collection of notes."""


# application (string) - The application storing the notes.
# misc (map:string) - Additional information about the note archive.
# name (string) - The name of the notes archive.


def add_noteFolder(graph, trace):
    """A folder containing notes."""


# application (string) - The application which stores the note folder.
# misc (map:string) - Additional information about the note archive.
# name (string) - The name of the notes folder.


def add_phoneCall(graph, trace):
    """A phone call."""


# application (string) - The application which received or made the phone call, for example "Skype".
# duration (integer) - The duration of the phone call in seconds.
# endsOn (date) - The date and time at which the phone call was terminated.
# from (string) - The phone number of the initiating party.
# index (integer) - The index of the phone call in phone calls list.
# misc (map:string) - Additional information on the phone call.
# startsOn (date) - The date and time at which the phone call was initiated.
# timestamps (map:date) - Additional timestamps for a phone call.
# to (string) - The receiver's phone number.
# type (string) - The type of a phone call,for example incoming, outgoing, missed.


def add_phoneCallLog(graph, trace):
    """A collection of phone calls."""


# application (string) - The application receiving or making the phone calls contained in this log.
# misc (map:string) - Additional information about the phoneCallLog.


def add_picture(graph, trace):
    """A picture is a two-dimensional visual representation."""


# application (string) - The application storing the pictures.
# aspectRatio (real) - The aspect ratio of the picture, <1.0 indicating portrait orientation >1.0 indicating landscape orientation.
# camera (string) - The name/make of the camera that was used for taking the picture.
# digitizedOn (date) - The time at which the picture was digitized.
# exif (map:string) - The EXIF (Exchangeable Image File Format) information of the picture; the metadata contained in the picture.
# format (string) - The format of a picture, for example jpg or png.
# height (integer) - The height of the picture in pixels.
# index (integer) - The index of the picture in the container.
# misc (map:string) - Additional information about the picture.
# modifiedOn (date) - The time at which the content of the picture was modified.
# originalTakenOn (date) - The time at which the picture was originally taken.
# photoDnaHash (binary) - The PhotoDNA Robust Hash of the picture.
# type (string) - The type of a picture, for example a thumbnail.
# width (integer) - The width of the picture in pixels.


def add_process(graph, trace):
    """A process that runs (or exited) at the moment that the memory dump was created."""


# createdOn (date) - The date and time at which the process was created.
# exitStatus (integer) - A small number passed from the process to the parent process when it has finished executing. In general, 0 indicates successful termination, any other number indicates a failure.
# exitedOn (date) - The time at which the process exited.
# id (string) - The identifier of the process.
# memoryAddress (string) - The address (in memory) of the process.
# name (string) - The name of the process.
# parentId (string) - The identifier of the process that created this process.
# status (string) - The status of the process, for example active or exited.
# user (string) - The user that owns the process.


def add_registry(graph, trace):
    """A registry hive contains configuration of a Microsoft Windows operating systems."""


# misc (map:string) - Additional information about the registry.
# type (string) - The type of a registry hive.


def add_registryEntry(graph, trace):
    """A registry entry is a configuration of a Microsoft Windows operating systems."""


# className (string) - The value of a hidden attribute of the registry key often referred to as class name.
# key (string) - The flattend path, separated by slashes, of the entry in the registry hyve.
# misc (map:string) - Additional information about the registryEntry.
# modifiedOn (date) - The time at which the content of the registry key was last modified.
# name (string) - The name of the registry key.
# type (string) - The data type of the registry value.
# value (string) - The registry value is the optional value stored with the key.


def add_signed(graph, trace):
    """Data signed with a private key."""


# misc (map:string) - Additional information on the signed data.
# serialNumbers (list:string) - Serial numbers of the signer certificates.
# type (string) - The type of the signed data.


def add_task(graph, trace):
    """An entry on a to-do list."""


# application (string) - The application storing this task.
# categories (map:string) - Categories applied to the event.
# createdOn (date) - The date and time at which the task was created.
# duration (integer) - The duration of the task.
# endsOn (date) - The date and time at which the task ends.
# labels (map:string) - Named and colored label.
# misc (map:string) - Additional information on the task.
# modifiedOn (date) - The date and time at which the task was last modified.
# owner (string) - The owner of the task.
# priority (string) - The priority of the task.
# recurrence (string) - Recurrence of the event.
# remindOn (date) - The date and time at which a reminder is given about the calendar entry.
# startsOn (date) - The date and time at which the task starts.
# status (string) - The status of the event, for instance accepted, pending or cancelled.
# subject (string) - The subject of the task.
# timestamps (map:date) - Additional timestamps for this task.
# type (string) - The type of task to be performed.


def add_taskList(graph, trace):
    """A collection of to-do tasks."""


# application (string) - The application storing this task list.
# misc (map:string) - Additional information about the to-do list.
# owner (string) - The owner of the to-do list.


def add_textMessage(graph, trace):
    """A (mobile) text message."""


# application (string) - The application sending or receiving this text message.
# from (string) - The sender's phone number.
# index (integer) - The index of the message in the text messages list.
# message (string) - The contents of the message.
# misc (map:string) - Additional information about the text message.
# read (boolean) - True if the text message has been read.
# sentOn (date) - The time at which the text message was sent.
# to (list:string) - The receivers' phone numbers.
# type (string) - the type of a text message, for example incoming, draft or outgoing.


def add_textMessageArchive(graph, trace):
    """A collection of text messages."""


# application (string) - The application sending or receiving text messages stored in this archive.
# misc (map:string) - Additional information about the text message archive.
# name (string) - The name of the text message archive.


def add_textMessageFolder(graph, trace):
    """A folder containing text messages."""


# messageCount (integer) - The number of text messages in the text message folder.
# misc (map:string) - Additional information about the text message folder.
# name (string) - The name of the text message folder.
# unreadMessageCount (integer) - The number of unread text messages in the text message folder.


def add_thumbnail(graph, trace):
    """A miniature view of a picture."""


# createdOn (date) - The date and time at which the thumbnail was created.
# misc (map:string) - Additional information about the thumbnail.
# modifiedOn (date) - The date and time at which the thumbnail was modified.
# type (string) - The type of thumbnail.


def add_thumbnailArchive(graph, trace):
    """A collection of thumbnails."""


# application (string) - The application maintaining the thumbnail archive.
# misc (map:string) - Additional information about the thumbnail archive.


def add_track(graph, trace):
    """A sequence of GPS locations marking a single track."""


# application (string) - The application storing this track.
# endsOn (date) - The latest date and time of any gps location of the track.
# misc (map:string) - Additional information about the track.
# name (string) - The name of the track.
# startsOn (date) - The earliest date and time of any gps location of the track.


def add_unallocated(graph, trace):
    """An unallocated trace is a part of an image that is not allocated to a physical trace."""


# path (string) - The path where the unallocated space can be found in the filesystem.


def add_url(graph, trace):
    """A uniform resource locator"""


# fragment (string) - Fragment pointing to a specific part in the resource.
# fragments (map:string) - Fragment split into its separate parts.
# host (string) - Domain name or IP address where the resource is located.
# misc (map:string) - Additional information about the url.
# password (string) - Password used to authenticate to this resource.
# path (string) - Path where the resource is located on the server.
# port (integer) - Port on which communication takes place.
# queries (map:string) - Query split into its separate parts.
# query (string) - Query passed to the resource.
# scheme (string) - Identifies the type of URL.
# username (string) - Username used to authenticate to this resource.


def add_video(graph, trace):
    """A media trace that contains video."""


# aspectRatio (real) - The aspect ratio of the video, <1.0 indicating portrait orientation >1.0 indicating landscape orientation.
# bitrate (integer) - The bitrate of the video in bits per second.
# createdOn (date) - The date and time at which the video was created.
# duration (integer) - The duration of the video in seconds.
# format (string) - The format of the video. For example: mp4.
# framerate (integer) - The framerate of the video in frames per second.
# height (integer) - The height the video in pixels.
# metadata (map:string) - Video metadata, e.g. title, genre, artist.
# misc (map:string) - Additional information about the video.
# processedStream (integer) - Video stream index used for image processing.
# streams (list:string) - Stream type per index plus codec, for example audio: MP3 (MPEG audio layer 3), video: FLV / Sorenson Spark / Sorenson H.263 (Flash Video).
# type (string) - The type of video.
# width (integer) - The width of the video in pixels.


def add_volume(graph, trace):
    """A volume is a single accessible storage area with a single file system."""


# description (string) - A free text description of the volume.
# id (string) - The unique identifier of the volume.
# misc (map:string) - Additional information about the volume.
# name (string) - The name of the volume.
# sectorSize (integer) - The sector size of the volume.
# timestamps (map:date) - volume timestamps.
