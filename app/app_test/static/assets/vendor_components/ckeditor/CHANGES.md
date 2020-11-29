CKEditor 4 Changelog
====================

## CKEditor 4.9.1

Fixed Issues:

* [#1835](https://github.com/ckeditor/ckeditor-dev/issues/1835): Fixed: Integration between [CKFinder](https://ckeditor.com/ckeditor-4/ckfinder/) and [File Browser](https://ckeditor.com/cke4/addon/filebrowser) plugin does not work.

## CKEditor 4.9

New Features:

* [#932](https://github.com/ckeditor/ckeditor-dev/issues/932): Introduced Easy Image feature for inserting images that are automatically rescaled, optimized, responsive and delivered through a blazing-fast CDN. Three new plugins were added to support it:
    * [Easy Image](https://ckeditor.com/cke4/addon/easyimage),
    * [Cloud Services](https://ckeditor.com/cke4/addon/cloudservices)
    * [Image Base](https://ckeditor.com/cke4/addon/imagebase)
* [#1338](https://github.com/ckeditor/ckeditor-dev/issues/1338): Keystroke labels are displayed for function keys (like F7, F8).
* [#643](https://github.com/ckeditor/ckeditor-dev/issues/643): The [File Browser](https://ckeditor.com/cke4/addon/filebrowser) plugin can now upload files using XHR requests. This allows for setting custom HTTP headers using the [`config.fileTools_requestHeaders`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-fileTools_requestHeaders) configuration option.
* [#1365](https://github.com/ckeditor/ckeditor-dev/issues/1365): The [File Browser](https://ckeditor.com/cke4/addon/filebrowser) plugin uses XHR requests by default.
* [#1399](https://github.com/ckeditor/ckeditor-dev/issues/1399): Added the possibility to set [`CKEDITOR.config.startupFocus`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-startupFocus) as `start` or `end` to specify where the editor focus should be after the initialization.
* [#1441](https://github.com/ckeditor/ckeditor-dev/issues/1441): The [Magic Line](https://ckeditor.com/cke4/addon/magicline) plugin line element can now be identified by the `data-cke-magic-line="1"` attribute.

Fixed Issues:

* [#595](https://github.com/ckeditor/ckeditor-dev/issues/595): Fixed: Pasting does not work on mobile devices.
* [#869](https://github.com/ckeditor/ckeditor-dev/issues/869): Fixed: Empty selection clears cached clipboard data in the editor.
* [#1419](https://github.com/ckeditor/ckeditor-dev/issues/1419): Fixed: The [Widget Selection](https://ckeditor.com/cke4/addon/widgetselection) plugin selects the editor content with the <kbd>Alt+A</kbd> key combination on Windows.
* [#1274](https://github.com/ckeditor/ckeditor-dev/issues/1274): Fixed: [Balloon Toolbar](https://ckeditor.com/cke4/addon/balloontoolbar) does not match a single selected image using the [`contextDefinition.cssSelector`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.balloontoolbar.contextDefinition-property-cssSelector) matcher.
* [#1232](https://github.com/ckeditor/ckeditor-dev/issues/1232): Fixed: [Balloon Toolbar](https://ckeditor.com/cke4/addon/balloontoolbar) buttons should be registered as focusable elements.
* [#1342](https://github.com/ckeditor/ckeditor-dev/issues/1342): Fixed: [Balloon Toolbar](https://ckeditor.com/cke4/addon/balloontoolbar) should be re-positioned after the [`change`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-change) event.
* [#1426](https://github.com/ckeditor/ckeditor-dev/issues/1426): [IE8-9] Fixed: Missing [Balloon Toolbar](https://ckeditor.com/cke4/addon/balloontoolbar) background in the [Kama](https://ckeditor.com/cke4/addon/kama) skin. Thanks to [Christian Elmer](https://github.com/keinkurt)!
* [#1470](https://github.com/ckeditor/ckeditor-dev/issues/1470): Fixed: [Balloon Toolbar](https://ckeditor.com/cke4/addon/balloontoolbar) is not visible after drag and drop of a widget it is attached to.
* [#1048](https://github.com/ckeditor/ckeditor-dev/issues/1048): Fixed: [Balloon Panel](https://ckeditor.com/cke4/addon/balloonpanel) is not positioned properly when a margin is added to its non-static parent.
* [#889](https://github.com/ckeditor/ckeditor-dev/issues/889): Fixed: Unclear error message for width and height fields in the [Image](https://ckeditor.com/cke4/addon/image) and [Enhanced Image](https://ckeditor.com/cke4/addon/image2) plugins.
* [#859](https://github.com/ckeditor/ckeditor-dev/issues/859): Fixed: Cannot edit a link after a double-click on the text in the link.
* [#1013](https://github.com/ckeditor/ckeditor-dev/issues/1013): Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) does not work correctly with the [`config.forcePasteAsPlainText`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-forcePasteAsPlainText) option.
* [#1356](https://github.com/ckeditor/ckeditor-dev/issues/1356): Fixed: [Border parse function](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools.style.parse-method-border) does not allow spaces in the color value.
* [#1010](https://github.com/ckeditor/ckeditor-dev/issues/1010): Fixed: The CSS `border` shorthand property was incorrectly expanded ignoring the `border-color` style.
* [#1535](https://github.com/ckeditor/ckeditor-dev/issues/1535): Fixed: [Widget](https://ckeditor.com/cke4/addon/widget) mouseover border contrast is insufficient.
* [#1516](https://github.com/ckeditor/ckeditor-dev/issues/1516): Fixed: Fake selection allows removing content in read-only mode using the <kbd>Backspace</kbd> and <kbd>Delete</kbd> keys.
* [#1570](https://github.com/ckeditor/ckeditor-dev/issues/1570): Fixed: Fake selection allows cutting content in read-only mode using the <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>X</kbd> keys.
* [#1363](https://github.com/ckeditor/ckeditor-dev/issues/1363): Fixed: Paste notification is unclear and it might confuse users.

API Changes:

* [#1346](https://github.com/ckeditor/ckeditor-dev/issues/1346): [Balloon Toolbar](https://ckeditor.com/cke4/addon/balloontoolbar) [context manager API](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.balloontoolbar.contextManager) is now available in the [`pluginDefinition.init`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.pluginDefinition-method-init) method of the [requiring](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.pluginDefinition-property-requires) plugin.
* [#1530](https://github.com/ckeditor/ckeditor-dev/issues/1530): Added the possibility to use custom icons for [buttons](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR_ui_button.html).

Other Changes:

* Updated [SCAYT](https://ckeditor.com/cke4/addon/scayt) (Spell Check As You Type) and [WebSpellChecker](https://ckeditor.com/cke4/addon/wsc) (WSC) plugins:
	* SCAYT [`scayt_minWordLength`](https://docs.ckeditor.com/ckeditor4/latest/api/CKEDITOR_config.html#scayt_minWordLength) configuration option now defaults to 3 instead of 4.
	* SCAYT default number of suggested words in the context menu changed to 3.
	* [#90](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/90): Fixed: Selection is lost on link creation if SCAYT highlights the word.
	* Fixed: SCAYT crashes when the browser `localStorage` is disabled.
	* [IE11] Fixed: `Unable to get property type of undefined or null reference` error in the browser console when SCAYT is disabled/enabled.
	* [#46](https://github.com/WebSpellChecker/ckeditor-plugin-wsc/issues/46): Fixed: Editing is blocked when remote spell checker server is offline.
	* Fixed: User Dictionary cannot be created in WSC due to `You already have the dictionary` error.
	* Fixed: Words with apostrophe `'` on the replacement make the WSC dialog inaccessible.
	* Fixed: SCAYT/WSC causes the `Uncaught TypeError` error in the browser console.
* [#1337](https://github.com/ckeditor/ckeditor-dev/issues/1337): Updated the samples layout with the new CKEditor 4 logo and color scheme.
* [#1591](https://github.com/ckeditor/ckeditor-dev/issues/1591): CKBuilder and language tools are now downloaded over HTTPS. Thanks to [August Detlefsen](https://github.com/augustd)!

## CKEditor 4.8

**Important Notes:**

* [#1249](https://github.com/ckeditor/ckeditor-dev/issues/1249): Enabled the [Upload Image](https://ckeditor.com/cke4/addon/uploadimage) plugin by default in standard and full presets. Also, it will no longer log an error in case of missing [`config.imageUploadUrl`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-imageUploadUrl) property.

New Features:

* [#933](https://github.com/ckeditor/ckeditor-dev/issues/933): Introduced [Balloon Toolbar](https://ckeditor.com/cke4/addon/balloontoolbar) plugin.
* [#662](https://github.com/ckeditor/ckeditor-dev/issues/662): Introduced image inlining for the [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin.
* [#468](https://github.com/ckeditor/ckeditor-dev/issues/468): [Edge] Introduced support for the Clipboard API.
* [#607](https://github.com/ckeditor/ckeditor-dev/issues/607): Manually inserted Hex color is prefixed with a hash character (`#`) if needed. It ensures a valid Hex color value is used when setting the table cell border or background color with the [Color Dialog](https://ckeditor.com/cke4/addon/colordialog) window.
* [#584](https://github.com/ckeditor/ckeditor-dev/issues/584): [Font size and Family](https://ckeditor.com/cke4/addon/font) and [Format](https://ckeditor.com/cke4/addon/format) drop-downs are not toggleable anymore. Default option to reset styles added.
* [#856](https://github.com/ckeditor/ckeditor-dev/issues/856): Introduced the [`CKEDITOR.tools.keystrokeToArray`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools-method-keystrokeToArray) method. It converts a keystroke into its string representation, returning every key name as a separate array element.
* [#1053](https://github.com/ckeditor/ckeditor-dev/issues/1053): Introduced the [`CKEDITOR.tools.object.merge`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools.object-method-merge) method. It allows to merge two objects, returning the new object with all properties from both objects deeply cloned.
* [#1073](https://github.com/ckeditor/ckeditor-dev/issues/1073): Introduced the [`CKEDITOR.tools.array.every`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools.array-method-every) method. It invokes a given test function on every array element and returns `true` if all elements pass the test.

Fixed Issues:

* [#796](https://github.com/ckeditor/ckeditor-dev/issues/796): Fixed: A list is pasted from OneNote in the reversed order.
* [#834](https://github.com/ckeditor/ckeditor-dev/issues/834): [IE9-11] Fixed: The editor does not save the selected state of radio buttons inserted by the [Form Elements](https://ckeditor.com/cke4/addon/forms) plugin.
* [#704](https://github.com/ckeditor/ckeditor-dev/issues/704): [Edge] Fixed: Using <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>Z</kbd> breaks widget structure.
* [#591](https://github.com/ckeditor/ckeditor-dev/issues/591): Fixed: A column is inserted in a wrong order inside the table if any cell has a vertical split.
* [#787](https://github.com/ckeditor/ckeditor-dev/issues/787): Fixed: Using Cut inside a nested table does not cut the selected content.
* [#842](https://github.com/ckeditor/ckeditor-dev/issues/842): Fixed: List style not restored when toggling list indent level in the [Indent List](https://ckeditor.com/cke4/addon/indentlist) plugin.
* [#711](https://github.com/ckeditor/ckeditor-dev/issues/711): Fixed: Dragging widgets should only work with the left mouse button.
* [#862](https://github.com/ckeditor/ckeditor-dev/issues/862): Fixed: The "Object Styles" group in the [Styles Combo](https://ckeditor.com/cke4/addon/stylescombo) plugin is visible only if the whole element is selected.
* [#994](https://github.com/ckeditor/ckeditor-dev/pull/994): Fixed: Typo in the [`CKEDITOR.focusManager.focus`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.focusManager-method-focus) API documentation. Thanks to [benjy](https://github.com/benjy)!
* [#1014](https://github.com/ckeditor/ckeditor-dev/issues/1014): Fixed: The [Table Tools](https://ckeditor.com/cke4/addon/tabletools) Cell Properties dialog is now [Advanced Content Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_acf) aware &mdash; it is not possible to change the cell width or height if corresponding styles are disabled.
* [#877](https://github.com/ckeditor/ckeditor-dev/issues/877): Fixed: A list with custom bullets with exotic characters crashes the editor when [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#605](https://github.com/ckeditor/ckeditor-dev/issues/605): Fixed: Inline widgets do not preserve trailing spaces.
* [#1008](https://github.com/ckeditor/ckeditor-dev/issues/1008): Fixed: Shorthand Hex colors from the [`config.colorButton_colors`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-colorButton_colors) option are not correctly highlighted in the [Color Button](https://ckeditor.com/cke4/addon/colorbutton) Text Color or Background Color panel.
* [#1094](https://github.com/ckeditor/ckeditor-dev/issues/1094): Fixed: Widget definition [`upcast`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget.definition-property-upcasts) methods are called for every element.
* [#1057](https://github.com/ckeditor/ckeditor-dev/issues/1057): Fixed: The [Notification](https://ckeditor.com/addon/notification) plugin overwrites Web Notifications API due to leakage to the global scope.
* [#1068](https://github.com/ckeditor/ckeditor-dev/issues/1068): Fixed: Upload widget paste listener ignores changes to the [`uploadWidgetDefinition`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.fileTools.uploadWidgetDefinition).
* [#921](https://github.com/ckeditor/ckeditor-dev/issues/921): Fixed: [Edge] CKEditor erroneously perceives internal copy and paste as type "external".
* [#1213](https://github.com/ckeditor/ckeditor-dev/issues/1213): Fixed: Multiple images uploaded using [Upload Image](https://ckeditor.com/cke4/addon/uploadimage) plugin are randomly duplicated or mangled.
* [#532](https://github.com/ckeditor/ckeditor-dev/issues/532): Fixed: Removed an outdated user guide link from the [About](https://ckeditor.com/cke4/addon/about) dialog.
* [#1221](https://github.com/ckeditor/ckeditor-dev/issues/1221): Fixed: Invalid CSS loaded by [Balloon Panel](https://ckeditor.com/cke4/addon/balloonpanel) plugin when [`config.skin`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-skin) is loaded using a custom path.
* [#522](https://github.com/ckeditor/ckeditor-dev/issues/522): Fixed: Widget selection is not removed when widget is inside table cell with [Table Selection](https://ckeditor.com/cke4/addon/tableselection) plugin enabled.
* [#1027](https://github.com/ckeditor/ckeditor-dev/issues/1027): Fixed: Cannot add multiple images to the table with [Table Selection](https://ckeditor.com/cke4/addon/tableselection) plugin in certain situations.
* [#1069](https://github.com/ckeditor/ckeditor-dev/issues/1069): Fixed: Wrong shape processing by [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin.
* [#995](https://github.com/ckeditor/ckeditor-dev/issues/995): Fixed: Hyperlinked image gets inserted twice by [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin.
* [#1287](https://github.com/ckeditor/ckeditor-dev/issues/1287): Fixed: [Widget](https://ckeditor.com/cke4/addon/widget) plugin throws exception if included in editor build but not loaded into editor's instance.

API Changes:

* [#1097](https://github.com/ckeditor/ckeditor-dev/issues/1097): Widget [`upcast`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget.definition-property-upcast) methods are now called in the [widget definition's](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget-property-definition) context.
* [#1118](https://github.com/ckeditor/ckeditor-dev/issues/1118): Added the `show` option in the [`balloonPanel.attach`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.ui.balloonPanel-method-attach) method, allowing to attach a hidden [Balloon Panel](https://ckeditor.com/cke4/addon/balloonpanel) instance.
* [#1145](https://github.com/ckeditor/ckeditor-dev/issues/1145): Added the [`skipNotifications`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.fileTools.uploadWidgetDefinition-property-skipNotifications) option to the [`CKEDITOR.fileTools.uploadWidgetDefinition`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.fileTools.uploadWidgetDefinition), allowing to switch off default notifications displayed by upload widgets.

Other Changes:

* [#815](https://github.com/ckeditor/ckeditor-dev/issues/815): Removed Node.js dependency from the CKEditor build script.
* [#1041](https://github.com/ckeditor/ckeditor-dev/pull/1041), [#1131](https://github.com/ckeditor/ckeditor-dev/issues/1131): Updated URLs pointing to [CKSource](https://cksource.com/) and [CKEditor](https://ckeditor.com/) resources after the launch of new websites.

## CKEditor 4.7.3

New Features:

* [#568](https://github.com/ckeditor/ckeditor-dev/issues/568): Added possibility to adjust nested editables' filters using the [`CKEDITOR.filter.disallowedContent`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.filter-property-disallowedContent) property.

Fixed Issues:

* [#554](https://github.com/ckeditor/ckeditor-dev/issues/554): Fixed: [`change`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-change) event not fired when typing the first character after pasting into the editor. Thanks to [Daniel Miller](https://github.com/millerdev)!
* [#566](https://github.com/ckeditor/ckeditor-dev/issues/566): Fixed: The CSS `border` shorthand property with zero width (`border: 0px solid #000;`) causes the table to have the border attribute set to 1.
* [#779](https://github.com/ckeditor/ckeditor-dev/issues/779): Fixed: The [Remove Format](https://ckeditor.com/cke4/addon/removeformat) plugin removes elements with language definition inserted by the [Language](https://ckeditor.com/cke4/addon/language) plugin.
* [#423](https://github.com/ckeditor/ckeditor-dev/issues/423): Fixed: The [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin pastes paragraphs into the editor even if [`CKEDITOR.config.enterMode`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-enterMode) is set to `CKEDITOR.ENTER_BR`.
* [#719](https://github.com/ckeditor/ckeditor-dev/issues/719): Fixed: Image inserted using the [Enhanced Image](https://ckeditor.com/cke4/addon/image2) plugin can be resized when the editor is in [read-only mode](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_readonly).
* [#577](https://github.com/ckeditor/ckeditor-dev/issues/577): Fixed: The "Delete Columns" command provided by the [Table Tools](https://ckeditor.com/cke4/addon/tabletools) plugin throws an error when trying to delete columns.
* [#867](https://github.com/ckeditor/ckeditor-dev/issues/867): Fixed: Typing into a selected table throws an error.
* [#817](https://github.com/ckeditor/ckeditor-dev/issues/817): Fixed: The [Save](https://ckeditor.com/cke4/addon/save) plugin does not work in [Source Mode](https://ckeditor.com/cke4/addon/sourcearea).

Other Changes:

* Updated the [WebSpellChecker](https://ckeditor.com/cke4/addon/wsc) plugin:
	* [#40](https://github.com/WebSpellChecker/ckeditor-plugin-wsc/issues/40): Fixed: IE10 throws an error when spell checking is started.
* [#800](https://github.com/ckeditor/ckeditor-dev/issues/800): Added the [`CKEDITOR.dom.selection.isCollapsed`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.selection-method-isCollapsed) method which is a simpler way to check if the selection is collapsed.
* [#830](https://github.com/ckeditor/ckeditor-dev/issues/830): Added an option to define which dialog tab should be shown by default when creating [`CKEDITOR.dialogCommand`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dialogCommand).

## CKEditor 4.7.2

New Features:

* [#455](https://github.com/ckeditor/ckeditor-dev/issues/455): Added [Advanced Content Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_acf) integration with the [Justify](https://ckeditor.com/cke4/addon/justify) plugin.

Fixed Issues:

* [#663](https://github.com/ckeditor/ckeditor-dev/issues/663): [Chrome] Fixed: Clicking the scrollbar throws an `Uncaught TypeError: element.is is not a function` error.
* [#694](https://github.com/ckeditor/ckeditor-dev/pull/694): Refactoring in the [Table Selection](https://ckeditor.com/cke4/addon/tableselection) plugin:
  * [#520](https://github.com/ckeditor/ckeditor-dev/issues/520): Fixed: Widgets cannot be properly pasted into a table cell.
  * [#460](https://github.com/ckeditor/ckeditor-dev/issues/460): Fixed: Editor gone after pasting into an editor within a table.
* [#579](https://github.com/ckeditor/ckeditor-dev/issues/579): Fixed: Internal `cke_table-faked-selection-table` class is visible in the Stylesheet Classes field of the [Table Properties](https://ckeditor.com/cke4/addon/table) dialog.
* [#545](https://github.com/ckeditor/ckeditor-dev/issues/545): [Edge] Fixed: Error thrown when pressing the [Select All](https://ckeditor.com/cke4/addon/selectall) button in [Source Mode](https://ckeditor.com/cke4/addon/sourcearea).
* [#582](https://github.com/ckeditor/ckeditor-dev/issues/582): Fixed: Double slash in the path to stylesheet needed by the [Table Selection](https://ckeditor.com/cke4/addon/tableselection) plugin. Thanks to [Marius Dumitru Florea](https://github.com/mflorea)!
* [#491](https://github.com/ckeditor/ckeditor-dev/issues/491): Fixed: Unnecessary dependency on the [Editor Toolbar](https://ckeditor.com/cke4/addon/toolbar) plugin inside the [Notification](https://ckeditor.com/cke4/addon/notification) plugin.
* [#646](https://github.com/ckeditor/ckeditor-dev/issues/646): Fixed: Error thrown into the browser console after opening the [Styles Combo](https://ckeditor.com/cke4/addon/stylescombo) plugin menu in the editor without any selection.
* [#501](https://github.com/ckeditor/ckeditor-dev/issues/501): Fixed: Double click does not open the dialog for modifying anchors inserted via the [Link](https://ckeditor.com/cke4/addon/link) plugin.
* [#9780](https://dev.ckeditor.com/ticket/9780): [IE8-9] Fixed: Clicking inside an empty [read-only](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-property-readOnly) editor throws an error.
* [#16820](https://dev.ckeditor.com/ticket/16820): [IE10] Fixed: Clicking below a single horizontal rule throws an error.
* [#426](https://github.com/ckeditor/ckeditor-dev/issues/426): Fixed: The [`range.cloneContents`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.range-method-cloneContents) method selects the whole element when the selection starts at the beginning of that element.
* [#644](https://github.com/ckeditor/ckeditor-dev/issues/644): Fixed: The [`range.extractContents`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.range-method-extractContents) method returns an incorrect result when multiple nodes are selected.
* [#684](https://github.com/ckeditor/ckeditor-dev/issues/684): Fixed: The [`elementPath.contains`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.elementPath-method-contains) method incorrectly excludes the last element instead of root when the `fromTop` parameter is set to `true`.

Other Changes:

* Updated the [SCAYT](https://ckeditor.com/cke4/addon/scayt) (Spell Check As You Type) plugin:
	* [#148](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/148): Fixed: SCAYT leaves underlined word after the CKEditor Replace dialog corrects it.
* [#751](https://github.com/ckeditor/ckeditor-dev/issues/751): Added the [`CKEDITOR.dom.nodeList.toArray`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.nodeList-method-toArray) method which returns an array representation of a [node list](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.nodeList).

## CKEditor 4.7.1

New Features:

* Added a new Mexican Spanish localization. Thanks to [David Alexandro Rodriguez](https://www.transifex.com/user/profile/darsco16/)!
* [#413](https://github.com/ckeditor/ckeditor-dev/issues/413): Added Paste as Plain Text keyboard shortcut to the [Accessibility Help](https://ckeditor.com/cke4/addon/a11yhelp) instructions.

Fixed Issues:

* [#515](https://github.com/ckeditor/ckeditor-dev/issues/515): [Chrome] Fixed: Mouse actions on CKEditor scrollbar throw an exception when the [Table Selection](https://ckeditor.com/cke4/addon/tableselection) plugin is loaded.
* [#493](https://github.com/ckeditor/ckeditor-dev/issues/493): Fixed: Selection started from a nested table causes an error in the browser while scrolling down.
* [#415](https://github.com/ckeditor/ckeditor-dev/issues/415): [Firefox] Fixed: <kbd>Enter</kbd> key breaks the table structure when pressed in a table selection.
* [#457](https://github.com/ckeditor/ckeditor-dev/issues/457): Fixed: Error thrown when deleting content from the editor with no selection.
* [#478](https://github.com/ckeditor/ckeditor-dev/issues/478): [Chrome] Fixed:  Error thrown by the [Enter Key](https://ckeditor.com/cke4/addon/enterkey) plugin when pressing <kbd>Enter</kbd> with no selection.
* [#424](https://github.com/ckeditor/ckeditor-dev/issues/424): Fixed: Error thrown by [Tab Key Handling](https://ckeditor.com/cke4/addon/tab) and [Indent List](https://ckeditor.com/cke4/addon/indentlist) plugins when pressing <kbd>Tab</kbd> with no selection in inline editor.
* [#476](https://github.com/ckeditor/ckeditor-dev/issues/476): Fixed: Anchors inserted with the [Link](https://ckeditor.com/cke4/addon/link) plugin on collapsed selection cannot be edited.
* [#417](https://github.com/ckeditor/ckeditor-dev/issues/417): Fixed: The [Table Resize](https://ckeditor.com/cke4/addon/tableresize) plugin throws an error when used with a table with only header or footer rows.
* [#523](https://github.com/ckeditor/ckeditor-dev/issues/523): Fixed: The [`editor.getCommandKeystroke`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getCommandKeystroke) method does not obtain the correct keystroke.
* [#534](https://github.com/ckeditor/ckeditor-dev/issues/534): [IE] Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) does not work in Quirks Mode.
* [#450](https://github.com/ckeditor/ckeditor-dev/issues/450): Fixed: [`CKEDITOR.filter`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.filter) incorrectly transforms the `margin` CSS property.

## CKEditor 4.7

**Important Notes:**

* [#13793](https://dev.ckeditor.com/ticket/13793): The [`embed_provider`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-embed_provider) configuration option for the [Media Embed](https://ckeditor.com/cke4/addon/embed) and [Semantic Media Embed](https://ckeditor.com/cke4/addon/embedsemantic) plugins is no longer preset by default.
* The [UI Color](https://ckeditor.com/cke4/addon/uicolor) plugin now uses a custom color picker instead of the `YUI 2.7.0` library which has some known vulnerabilities (it's a security precaution, there was no security issue in CKEditor due to the way it was used).

New Features:

* [#16755](https://dev.ckeditor.com/ticket/16755): Added the [Table Selection](https://ckeditor.com/cke4/addon/tableselection) plugin that lets you select and manipulate an arbitrary rectangular table fragment (a few cells, a row or a column).
* [#16961](https://dev.ckeditor.com/ticket/16961): Added support for pasting from Microsoft Excel.
* [#13381](https://dev.ckeditor.com/ticket/13381): Dynamic code evaluation call in [`CKEDITOR.template`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.template) removed. CKEditor can now be used without the `unsafe-eval` Content Security Policy. Thanks to [Caridy Patiño](http://caridy.name)!
* [#16971](https://dev.ckeditor.com/ticket/16971): Added support for color in the `background` property containing also other styles for table cells in the [Table Tools](https://ckeditor.com/cke4/addon/tabletools) plugin.
* [#16847](https://dev.ckeditor.com/ticket/16847): Added support for parsing and inlining any formatting created using the Microsoft Word style system to the [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin.
* [#16818](https://dev.ckeditor.com/ticket/16818): Added table cell height parsing in the [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin.
* [#16850](https://dev.ckeditor.com/ticket/16850): Added a new [`config.enableContextMenu`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-enableContextMenu) configuration option for enabling and disabling the [context menu](https://ckeditor.com/cke4/addon/contextmenu).
* [#16937](https://dev.ckeditor.com/ticket/16937): The `command` parameter in [CKEDITOR.editor.getCommandKeystroke](http://docs.ckeditor.dev/#!/api/CKEDITOR.editor-method-getCommandKeystroke) now also accepts a command name as an argument.
* [#17010](https://dev.ckeditor.com/ticket/17010): The [`CKEDITOR.dom.range.shrink`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.range-method-shrink) method now allows for skipping bogus `<br>` elements.

Fixed Issues:

* [#16935](https://dev.ckeditor.com/ticket/16935): [Chrome] Fixed: Blurring the editor in [Source Mode](https://ckeditor.com/cke4/addon/sourcearea) throws an error.
* [#16825](https://dev.ckeditor.com/ticket/16825): [Chrome] Fixed: Error thrown when destroying a focused inline editor.
* [#16857](https://dev.ckeditor.com/ticket/16857): Fixed: <kbd>Ctrl+Shift+V</kbd> blocked by [Copy Formatting](https://ckeditor.com/cke4/addon/copyformatting).
* [#16845](https://dev.ckeditor.com/ticket/16845): [IE] Fixed: Cursor jumps to the top of the scrolled editor after focusing it when the [Copy Formatting](https://ckeditor.com/cke4/addon/copyformatting) plugin is enabled.
* [#16786](https://dev.ckeditor.com/ticket/16786): Fixed: Added missing translations for the [Copy Formatting](https://ckeditor.com/cke4/addon/copyformatting) plugin.
* [#14714](https://dev.ckeditor.com/ticket/14714): [WebKit/Blink] Fixed: Exception thrown on refocusing a blurred inline editor.
* [#16913](https://dev.ckeditor.com/ticket/16913): [Firefox, IE] Fixed: [Paste as Plain Text](https://ckeditor.com/cke4/addon/pastetext) keystroke does not work.
* [#16968](https://dev.ckeditor.com/ticket/16968): Fixed: [Safari] [Paste as Plain Text](https://ckeditor.com/cke4/addon/pastetext) is not handled by the editor.
* [#16912](https://dev.ckeditor.com/ticket/16912): Fixed: Exception thrown when a single image is pasted using [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#16821](https://dev.ckeditor.com/ticket/16821): Fixed: Extraneous `<span>` elements with `height` style stacked when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#16866](https://dev.ckeditor.com/ticket/16866): [IE, Edge] Fixed: Whitespaces not preserved when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#16860](https://dev.ckeditor.com/ticket/16860): Fixed: Paragraphs which only look like lists incorrectly transformed into them when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#16817](https://dev.ckeditor.com/ticket/16817): Fixed: When [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword), paragraphs are transformed into lists with some corrupted data.
* [#16833](https://dev.ckeditor.com/ticket/16833): [IE11] Fixed: Malformed list with headers [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#16826](https://dev.ckeditor.com/ticket/16826): [IE] Fixed: Superfluous paragraphs within lists [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#12465](https://dev.ckeditor.com/ticket/12465): Fixed: Cannot change the state of checkboxes or radio buttons if the properties dialog was invoked with a double-click.
* [#13062](https://dev.ckeditor.com/ticket/13062): Fixed: Impossible to unlink when the caret is at the edge of the link.
* [#13585](https://dev.ckeditor.com/ticket/13585): Fixed: Error when wrapping two adjacent `<div>` elements with a `<div>`.
* [#16811](https://dev.ckeditor.com/ticket/16811): Fixed: Table alignment is not preserved by the [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin.
* [#16810](https://dev.ckeditor.com/ticket/16810): Fixed: Vertical align in tables is not supported by the [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin.
* [#11956](https://dev.ckeditor.com/ticket/11956): [Blink, IE] Fixed: [Link](https://ckeditor.com/cke4/addon/link) dialog does not open on a double click on the second word of the link with a background color or other styles.
* [#10472](https://dev.ckeditor.com/ticket/10472): Fixed: Unable to use [Table Resize](https://ckeditor.com/cke4/addon/tableresize) on table header and footer.
* [#14762](https://dev.ckeditor.com/ticket/14762): Fixed: Hovering over an empty table (without rows or cells) throws an error when the [Table Resize](https://ckeditor.com/cke4/addon/tableresize) plugin is active.
* [#16777](https://dev.ckeditor.com/ticket/16777): [Edge] Fixed: The [Clipboard](https://ckeditor.com/cke4/addon/clipboard) plugin does not allow to drop widgets into the editor.
* [#14894](https://dev.ckeditor.com/ticket/14894): [Chrome] Fixed: The editor scrolls to the top after focusing or when a dialog is opened.
* [#14769](https://dev.ckeditor.com/ticket/14769): Fixed: URLs with '-' in host are not detected by the [Auto Link](https://ckeditor.com/cke4/addon/autolink) plugin.
* [#16804](https://dev.ckeditor.com/ticket/16804): Fixed: Focus is not on the first menu item when the user opens a context menu or a drop-down list from the editor toolbar.
* [#14407](https://dev.ckeditor.com/ticket/14407): [IE] Fixed: Non-editable widgets can be edited.
* [#16927](https://dev.ckeditor.com/ticket/16927): Fixed: An error thrown if a bundle containing the [Color Button](https://ckeditor.com/cke4/addon/colorbutton) plugin is run in ES5 strict mode. Thanks to [Igor Rubinovich](https://github.com/IgorRubinovich)!
* [#16920](https://dev.ckeditor.com/ticket/16920): Fixed: Several plugins not using the [Dialog](https://ckeditor.com/cke4/addon/dialog) plugin as a direct dependency.
* [PR#336](https://github.com/ckeditor/ckeditor-dev/pull/336): Fixed: Typo in [`CKEDITOR.getCss`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR-method-getCss) API documentation. Thanks to [knusperpixel](https://github.com/knusperpixel)!
* [#17027](https://dev.ckeditor.com/ticket/17027): Fixed: Command event data should be initialized as an empty object.
* Fixed the behavior of HTML parser when parsing `src`/`srcdoc` attributes of the `<iframe>` element in a CKEditor setup with ACF turned off and without the [Iframe Dialog](https://ckeditor.com/cke4/addon/iframe) plugin. The issue was originally reported as a security issue by [Sriramk21](https://twitter.com/sriramk21) from Pegasystems and was later downgraded by the security team into a normal issue due to the requirement of having ACF turned off. Disabling [Advanced Content Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_advanced_content_filter) is against [security best practices](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_best_practices-section-security), so the problem described above has not been considered a security issue as such.

Other Changes:

* Updated [SCAYT](https://ckeditor.com/cke4/addon/scayt) (Spell Check As You Type) and [WebSpellChecker](https://ckeditor.com/cke4/addon/wsc) plugins:
	* Fixed: DOM Exception after clicking "Remove Language" on a selected word with enabled [Language](https://ckeditor.com/cke4/addon/language) plugin in SCAYT.
* [#16958](https://dev.ckeditor.com/ticket/16958): Switched the default MathJax CDN provider for the [Mathematical Formulas](https://ckeditor.com/cke4/addon/mathjax) plugin from `cdn.mathjax.org` to [cdnjs](https://cdnjs.com/), due to closing of `cdn.mathjax.org` scheduled for April 30, 2017.
* [#16954](https://dev.ckeditor.com/ticket/16954): Removed the paste dialog.
* [#16982](https://dev.ckeditor.com/ticket/16982): Latest Safari now supports enhanced Clipboard API introduced in CKEditor 4.5.0.
* [#17025](https://dev.ckeditor.com/ticket/17025): Updated [Bender.js](https://github.com/benderjs/benderjs) to 0.4.2.

## CKEditor 4.6.2

New Features:

* [#16733](https://dev.ckeditor.com/ticket/16733): Added a new pastel color palette for the [Color Button](https://ckeditor.com/cke4/addon/colorbutton) plugin and a new [`config.colorButton_colorsPerRow`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-colorButton_colorsPerRow) configuration option for setting the number of rows in the color selector.
* [#16752](https://dev.ckeditor.com/ticket/16752): Added a new Azerbaijani localization. Thanks to the [Azerbaijani language team](https://www.transifex.com/ckeditor/teams/11143/az/)!
* [#13818](https://dev.ckeditor.com/ticket/13818): It is now possible to group [Widget](https://ckeditor.com/cke4/addon/widget) [style definitions](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_styles-section-widget-styles), so applying one style disables the other.

Fixed Issues:

* [#13446](https://dev.ckeditor.com/ticket/13446): [Chrome] Fixed: It is possible to type in an unfocused inline editor.
* [#14856](https://dev.ckeditor.com/ticket/14856): Fixed: [Font size and font family](https://ckeditor.com/cke4/addon/font) reset each other when modified at certain positions.
* [#16745](https://dev.ckeditor.com/ticket/16745): [Edge] Fixed: List items are lost when [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#16682](https://dev.ckeditor.com/ticket/16682): [Edge] Fixed: A list gets [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword) as a set of paragraphs. Added the [`config.pasteFromWord_heuristicsEdgeList`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-pasteFromWord_heuristicsEdgeList) configuration option.
* [#10373](https://dev.ckeditor.com/ticket/10373): Fixed: Context menu items can be dragged into the editor.
* [#16728](https://dev.ckeditor.com/ticket/16728): [IE] Fixed: [Copy Formatting](https://ckeditor.com/cke4/addon/copyformatting) breaks the editor in Quirks Mode.
* [#16795](https://dev.ckeditor.com/ticket/16795): [IE] Fixed: [Copy Formatting](https://ckeditor.com/cke4/addon/copyformatting) breaks the editor in Compatibility Mode.
* [#16675](https://dev.ckeditor.com/ticket/16675): Fixed: Styles applied with [Copy Formatting](https://ckeditor.com/cke4/addon/copyformatting) to a single table cell are applied to the whole table.
* [#16753](https://dev.ckeditor.com/ticket/16753): Fixed: [`element.setSize`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-setSize) sets incorrect editor dimensions if the border width is represented as a fraction of pixels.
* [#16705](https://dev.ckeditor.com/ticket/16705): [Firefox] Fixed: Unable to paste images as Base64 strings when using [Clipboard](https://ckeditor.com/cke4/addon/clipboard).
* [#14869](https://dev.ckeditor.com/ticket/14869): Fixed: JavaScript error is thrown when trying to use [Find](https://ckeditor.com/cke4/addon/find) in a [`<div>`-based editor](https://ckeditor.com/cke4/addon/divarea).

## CKEditor 4.6.1

New Features:

* [#16639](https://dev.ckeditor.com/ticket/16639): The `callback` parameter in the [CKEDITOR.ajax.post](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.ajax-method-post) method became optional.

Fixed Issues:

* [#11064](https://dev.ckeditor.com/ticket/11064): [Blink, WebKit] Fixed: Cannot select all editor content when a widget or a non-editable element is the first or last element of the content. Also fixes this issue in the [Select All](https://ckeditor.com/cke4/addon/selectall) plugin.
* [#14755](https://dev.ckeditor.com/ticket/14755): [Blink, WebKit, IE8] Fixed: Browser hangs when a table is inserted in the place of a selected list with an empty last item.
* [#16624](https://dev.ckeditor.com/ticket/16624): Fixed: Improved the [Color Button](https://ckeditor.com/cke4/addon/colorbutton) plugin which will now normalize the CSS `background` property if it only contains a color value. This fixes missing background colors when using [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#16600](https://dev.ckeditor.com/ticket/16600): [Blink, WebKit] Fixed: Error thrown occasionally by an uninitialized editable for multiple CKEditor instances on the same page.

## CKEditor 4.6

New Features:

* [#14569](https://dev.ckeditor.com/ticket/14569): Added a new, flat, default CKEditor skin called [Moono-Lisa](https://ckeditor.com/cke4/addon/moono-lisa). Refreshed default colors available in the [Color Button](https://ckeditor.com/cke4/addon/colorbutton) plugin ([Text Color and Background Color](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_colorbutton) feature).
* [#14707](https://dev.ckeditor.com/ticket/14707): Added a new [Copy Formatting](https://ckeditor.com/cke4/addon/copyformatting) feature to enable easy copying of styles between your document parts.
* Introduced the completely rewritten [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) plugin:
	* Backward incompatibility: The [`config.pasteFromWordRemoveFontStyles`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-pasteFromWordRemoveFontStyles) option now defaults to `false`. This option will be deprecated in the future. Use [Advanced Content Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_acf) to replicate the effect of setting it to `true`.
	* Backward incompatibility: The [`config.pasteFromWordNumberedHeadingToList`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-pasteFromWordNumberedHeadingToList) and [`config.pasteFromWordRemoveStyles`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-pasteFromWordRemoveStyles) options were dropped and no longer have any effect on pasted content.
	* Major improvements in preservation of list numbering, styling and indentation (nested lists with multiple levels).
	* Major improvements in document structure parsing that fix plenty of issues with distorted or missing content after paste.
* Added new translation: Occitan. Thanks to [Cédric Valmary](https://totenoc.eu/)!
* [#10015](https://dev.ckeditor.com/ticket/10015): Keyboard shortcuts (relevant to the operating system in use) will now be displayed in tooltips and context menus.
* [#13794](https://dev.ckeditor.com/ticket/13794): The [Upload Image](https://ckeditor.com/cke4/addon/uploadimage) feature now uses `uploaded.width/height` if set.
* [#12541](https://dev.ckeditor.com/ticket/12541): Added the [Upload File](https://ckeditor.com/cke4/addon/uploadfile) plugin that lets you upload a file by drag&amp;dropping it into the editor content.
* [#14449](https://dev.ckeditor.com/ticket/14449): Introduced the [Balloon Panel](https://ckeditor.com/cke4/addon/balloonpanel) plugin that lets you create stylish floating UI elements for the editor.
* [#12077](https://dev.ckeditor.com/ticket/12077): Added support for the HTML5 `download` attribute in link (`<a>`) elements. Selecting the "Force Download" checkbox in the [Link](https://ckeditor.com/cke4/addon/link) dialog will cause the linked file to be downloaded automatically. Thanks to [sbusse](https://github.com/sbusse)!
* [#13518](https://dev.ckeditor.com/ticket/13518): Introduced the [`additionalRequestParameters`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.fileTools.uploadWidgetDefinition-property-additionalRequestParameters) property for file uploads to make it possible to send additional information about the uploaded file to the server.
* [#14889](https://dev.ckeditor.com/ticket/14889): Added the [`config.image2_altRequired`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-image2_altRequired) option for the [Enhanced Image](https://ckeditor.com/cke4/addon/image2) plugin to allow making alternative text a mandatory field. Thanks to [Andrey Fedoseev](https://github.com/andreyfedoseev)!

Fixed Issues:

* [#9991](https://dev.ckeditor.com/ticket/9991): Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) should only normalize input data.
* [#7209](https://dev.ckeditor.com/ticket/7209): Fixed: Lists with 3 levels not [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword) correctly.
* [#14335](https://dev.ckeditor.com/ticket/14335): Fixed: Pasting a numbered list starting with a value different from "1" from Microsoft Word does not work correctly.
* [#14542](https://dev.ckeditor.com/ticket/14542): Fixed: Copying a numbered list from Microsoft Word does not preserve list formatting.
* [#14544](https://dev.ckeditor.com/ticket/14544): Fixed: Copying a nested list from Microsoft Word results in an empty list.
* [#14660](https://dev.ckeditor.com/ticket/14660): Fixed: [Pasting text from  Word](https://ckeditor.com/cke4/addon/pastefromword) breaks the styling in some cases.
* [#14867](https://dev.ckeditor.com/ticket/14867): [Firefox] Fixed: Text gets stripped when [pasting content from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#2507](https://dev.ckeditor.com/ticket/2507): Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) does not detect pasting a part of a paragraph.
* [#3336](https://dev.ckeditor.com/ticket/3336): Fixed: Extra blank row added on top of the content [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#6115](https://dev.ckeditor.com/ticket/6115): Fixed: When Right-to-Left text direction is applied to a table [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword), borders are missing on one side.
* [#6342](https://dev.ckeditor.com/ticket/6342): Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) filters out a basic text style when it is [configured to use attributes](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_basicstyles-section-custom-basic-text-style-definition).
* [#6457](https://dev.ckeditor.com/ticket/6457): [IE] Fixed: [Pasting from Word](https://ckeditor.com/cke4/addon/pastefromword) is extremely slow.
* [#6789](https://dev.ckeditor.com/ticket/6789): Fixed: The `mso-list: ignore` style is not handled properly when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#7262](https://dev.ckeditor.com/ticket/7262): Fixed: Lists in preformatted body disappear when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#7662](https://dev.ckeditor.com/ticket/7662): [Opera] Fixed: Extra empty number/bullet shown in the editor body when editing a multi-level list [pasted from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#7807](https://dev.ckeditor.com/ticket/7807): Fixed: Last item in a list not converted to a `<li>` element after [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#7950](https://dev.ckeditor.com/ticket/7950): [IE] Fixed: Content [from Word pasted](https://ckeditor.com/cke4/addon/pastefromword) differently than in other browsers.
* [#7982](https://dev.ckeditor.com/ticket/7982): Fixed: Multi-level lists get split into smaller ones when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#8231](https://dev.ckeditor.com/ticket/8231): [WebKit, Opera] Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) inserts empty paragraphs.
* [#8266](https://dev.ckeditor.com/ticket/8266): Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) inserts a blank line at the top.
* [#8341](https://dev.ckeditor.com/ticket/8341), [#7646](https://dev.ckeditor.com/ticket/7646): Fixed: Faulty removal of empty `<span>` elements in [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) content cleanup breaking content formatting.
* [#8754](https://dev.ckeditor.com/ticket/8754): [Firefox] Fixed: Incorrect pasting of multiple nested lists in [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#8983](https://dev.ckeditor.com/ticket/8983): Fixed: Alignment lost when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword) with [`config.enterMode`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-enterMode) set to [`CKEDITOR.ENTER_BR`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR-property-ENTER_BR).
* [#9331](https://dev.ckeditor.com/ticket/9331): [IE] Fixed: [Pasting text from Word](https://ckeditor.com/cke4/addon/pastefromword) creates a simple Caesar cipher.
* [#9422](https://dev.ckeditor.com/ticket/9422): Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) leaves an unwanted `color:windowtext` style.
* [#10011](https://dev.ckeditor.com/ticket/10011): [IE9-10] Fixed: [`config.pasteFromWordRemoveFontStyles`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-pasteFromWordRemoveFontStyles) is ignored under certain conditions.
* [#10643](https://dev.ckeditor.com/ticket/10643): Fixed: Differences between using <kbd>Ctrl+V</kbd> and pasting from the [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) dialog.
* [#10784](https://dev.ckeditor.com/ticket/10784): Fixed: Lines missing when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#11294](https://dev.ckeditor.com/ticket/11294): [IE10] Fixed: Font size is not preserved when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#11627](https://dev.ckeditor.com/ticket/11627): Fixed: Missing words when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#12784](https://dev.ckeditor.com/ticket/12784): Fixed: Bulleted list with custom bullets gets changed to a numbered list when [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#13174](https://dev.ckeditor.com/ticket/13174): Fixed: Data loss after [pasting from Word](https://ckeditor.com/cke4/addon/pastefromword).
* [#13828](https://dev.ckeditor.com/ticket/13828): Fixed: Widget classes should be added to the wrapper rather than the widget element.
* [#13829](https://dev.ckeditor.com/ticket/13829): Fixed: No class in [Widget](https://ckeditor.com/cke4/addon/widget) wrapper to identify the widget type.
* [#13519](https://dev.ckeditor.com/ticket/13519): Server response received when uploading files should be more flexible.

Other Changes:

* Updated [SCAYT](https://ckeditor.com/cke4/addon/scayt) (Spell Check As You Type) and [WebSpellChecker](https://ckeditor.com/cke4/addon/wsc) plugins:
 	* Support for the new default Moono-Lisa skin.
 	* [#121](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/121): Fixed: [Basic Styles](https://ckeditor.com/cke4/addon/basicstyles) do not work when SCAYT is enabled.
 	* [#125](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/125): Fixed: Inline styles are not continued when writing multiple lines of styled text with SCAYT enabled.
 	* [#127](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/127): Fixed: Uncaught TypeError after enabling SCAYT in the CKEditor `<div>` element.
 	* [#128](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/128): Fixed: Error thrown after enabling SCAYT caused by conflicts with RequireJS.

## CKEditor 4.5.11

**Security Updates:**

* [Severity: minor] Fixed the `target="_blank"` vulnerability reported by James Gaskell.

	Issue summary: If a victim had access to a spoofed version of ckeditor.com via HTTP (e.g. due to DNS spoofing, using a hacked public network or mailicious hotspot), then when using a link to the ckeditor.com website it was possible for the attacker to change the current URL of the opening page, even if the opening page was protected with SSL.

  An upgrade is recommended.

New Features:

* [#14747](https://dev.ckeditor.com/ticket/14747): The [Enhanced Image](https://ckeditor.com/cke4/addon/image2) caption now supports the link `target` attribute.
* [#7154](https://dev.ckeditor.com/ticket/7154): Added support for the "Display Text" field to the [Link](https://ckeditor.com/cke4/addon/link) dialog. Thanks to [Ryan Guill](https://github.com/ryanguill)!

Fixed Issues:

* [#13362](https://dev.ckeditor.com/ticket/13362): [Blink, WebKit] Fixed: Active widget element is not cached when it is losing focus and it is inside an editable element.
* [#13755](https://dev.ckeditor.com/ticket/13755): [Edge] Fixed: Pasting images does not work.
* [#13548](https://dev.ckeditor.com/ticket/13548): [IE] Fixed: Clicking the [elements path](https://ckeditor.com/cke4/addon/elementspath) disables Cut and Copy icons.
* [#13812](https://dev.ckeditor.com/ticket/13812): Fixed: When aborting file upload the placeholder for image is left.
* [#14659](https://dev.ckeditor.com/ticket/14659): [Blink] Fixed: Content scrolled to the top after closing the dialog in a [`<div>`-based editor](https://ckeditor.com/cke4/addon/divarea).
* [#14825](https://dev.ckeditor.com/ticket/14825): [Edge] Fixed: Focusing the editor causes unwanted scrolling due to dropped support for the `setActive` method.

## CKEditor 4.5.10

Fixed Issues:

* [#10750](https://dev.ckeditor.com/ticket/10750): Fixed: The editor does not escape the `font-style` family property correctly, removing quotes and whitespace from font names.
* [#14413](https://dev.ckeditor.com/ticket/14413): Fixed: The [Auto Grow](https://ckeditor.com/cke4/addon/autogrow) plugin with the [`config.autoGrow_onStartup`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-autoGrow_onStartup) option set to `true` does not work properly for an editor that is not visible.
* [#14451](https://dev.ckeditor.com/ticket/14451): Fixed: Numeric element ID not escaped properly. Thanks to [Jakub Chalupa](https://github.com/chaluja7)!
* [#14590](https://dev.ckeditor.com/ticket/14590): Fixed: Additional line break appearing after inline elements when switching modes. Thanks to [dpidcock](https://github.com/dpidcock)!
* [#14539](https://dev.ckeditor.com/ticket/14539): Fixed: JAWS reads "selected Blank" instead of "selected <widget name>" when selecting a widget.
* [#14701](https://dev.ckeditor.com/ticket/14701): Fixed: More precise labels for [Enhanced Image](https://ckeditor.com/cke4/addon/image2) and [Placeholder](https://ckeditor.com/cke4/addon/placeholder) widgets.
* [#14667](https://dev.ckeditor.com/ticket/14667): [IE] Fixed: Removing background color from selected text removes background color from the whole paragraph.
* [#14252](https://dev.ckeditor.com/ticket/14252): [IE] Fixed: Styles drop-down list does not always reflect the current style of the text line.
* [#14275](https://dev.ckeditor.com/ticket/14275): [IE9+] Fixed: `onerror` and `onload` events are not used in browsers it could have been used when loading scripts dynamically.

## CKEditor 4.5.9

Fixed Issues:

* [#10685](https://dev.ckeditor.com/ticket/10685): Fixed: Unreadable toolbar icons after updating to the new editor version. Fixed with [6876179](https://github.com/ckeditor/ckeditor-dev/commit/6876179db4ee97e786b07b8fd72e6b4120732185) in [ckeditor-dev](https://github.com/ckeditor/ckeditor-dev) and [6c9189f4](https://github.com/ckeditor/ckeditor-presets/commit/6c9189f46392d2c126854fe8889b820b8c76d291) in [ckeditor-presets](https://github.com/ckeditor/ckeditor-presets).
* [#14573](https://dev.ckeditor.com/ticket/14573): Fixed: Missing [Widget](https://ckeditor.com/cke4/addon/widget) drag handler CSS when there are multiple editor instances.
* [#14620](https://dev.ckeditor.com/ticket/14620): Fixed: Setting both the `min-height` style for the `<body>` element and the `height` style for the `<html>` element breaks the [Auto Grow](https://ckeditor.com/cke4/addon/autogrow) plugin.
* [#14538](https://dev.ckeditor.com/ticket/14538): Fixed: Keyboard focus goes into an embedded `<iframe>` element.
* [#14602](https://dev.ckeditor.com/ticket/14602): Fixed: The [`dom.element.removeAttribute()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-removeAttribute) method does not remove all attributes if no parameter is given.
* [#8679](https://dev.ckeditor.com/ticket/8679): Fixed: Better focus indication and ability to style the selected color in the [color picker dialog](https://ckeditor.com/cke4/addon/colordialog).
* [#11697](https://dev.ckeditor.com/ticket/11697): Fixed: Content is replaced ignoring the letter case setting in the [Find and Replace](https://ckeditor.com/cke4/addon/find) dialog window.
* [#13886](https://dev.ckeditor.com/ticket/13886): Fixed: Invalid handling of the [`CKEDITOR.style`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.style) instance with the `styles` property by [`CKEDITOR.filter`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.filter).
* [#14535](https://dev.ckeditor.com/ticket/14535): Fixed: CSS syntax corrections. Thanks to [mdjdenormandie](https://github.com/mdjdenormandie)!

## CKEditor 4.5.8

New Features:

* [#12440](https://dev.ckeditor.com/ticket/12440): Added the [`config.colorButton_enableAutomatic`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-colorButton_enableAutomatic) option to allow hiding the "Automatic" option in the [color picker](https://ckeditor.com/cke4/addon/colorbutton).

Fixed Issues:

* [#10448](https://dev.ckeditor.com/ticket/10448): Fixed: Lack of scrollbar in the [right-to-left text direction](https://ckeditor.com/cke4/addon/bidi).
* [#12707](https://dev.ckeditor.com/ticket/12707): Fixed: The order of table elements does not comply with the HTML specification.
* [#13756](https://dev.ckeditor.com/ticket/13756): [Edge] Fixed: Context menus are cut-off.

## CKEditor 4.5.7

New Features:

* [#14327](https://dev.ckeditor.com/ticket/14327): Added Swiss German localization. Thanks to [Miro Grenda](https://twitter.com/mirogrenda)!

Fixed Issues:

* [#13816](https://dev.ckeditor.com/ticket/13816): Introduced a new strategy for Filling Character handling to avoid changes in DOM. This fixes the following issues:
	* [#12727](https://dev.ckeditor.com/ticket/12727): [Blink] `IndexSizeError` when using the [Div Editing Area](https://ckeditor.com/cke4/addon/divarea) and [Content Templates](https://ckeditor.com/cke4/addon/templates) plugins.
	* [#13377](https://dev.ckeditor.com/ticket/13377): [Widget](https://ckeditor.com/cke4/addon/widget) plugin issue when typing in Korean.
	* [#13389](https://dev.ckeditor.com/ticket/13389): [Blink] [`editor.getData()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getData) fails when the cursor is next to an `<hr>` tag.
	* [#13513](https://dev.ckeditor.com/ticket/13513): [Blink, WebKit] [Div Editing Area](https://ckeditor.com/cke4/addon/divarea) and [`editor.getData()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getData) throw an error when an image is the only data in the editor.
* [#13884](https://dev.ckeditor.com/ticket/13884): [Firefox] Fixed: Copying and pasting a table results in just the first cell being pasted.
* [#14234](https://dev.ckeditor.com/ticket/14234): Fixed: URL input field is not marked as required in the [Media Embed](https://ckeditor.com/cke4/addon/embed) dialog.

## CKEditor 4.5.6

New Features:

* Introduced the [`CKEDITOR.tools.getCookie()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools-method-getCookie) and [`CKEDITOR.tools.setCookie()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools-method-setCookie) methods for accessing cookies.
* Introduced the [`CKEDITOR.tools.getCsrfToken()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools-method-getCsrfToken) method. The CSRF token is now automatically sent by the [File Browser](https://ckeditor.com/cke4/addon/filebrowser) and [File Tools](https://ckeditor.com/cke4/addon/filetools) plugins during file uploads. The server-side upload handlers may check it and use it to additionally secure the communication.

Other Changes:

* Updated [SCAYT](https://ckeditor.com/cke4/addon/scayt) (Spell Check As You Type):
	- New features:
		- CKEditor [Language](https://ckeditor.com/cke4/addon/language) plugin support.
		- CKEditor [Placeholder](https://ckeditor.com/cke4/addon/placeholder) plugin support.
		- [Drag&Drop](https://sdk.ckeditor.com/samples/fileupload.html) support.
		- **Experimental** [GRAYT](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-grayt_autoStartup) (Grammar As You Type) functionality.
	- Fixed issues:
		* [#98](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/98): SCAYT affects dialog double-click. Fixed in SCAYT core.
		* [#102](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/102): SCAYT core performance enhancements.
		* [#104](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/104): SCAYT's spans leak into the clipboard and after pasting.
		* [#105](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/105): A JavaScript error fired in case of multiple instances of CKEditor on one page.
		* [#107](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/107): SCAYT should not check non-editable parts of content.
		* [#108](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/108): Latest SCAYT copies the ID of the editor element to the iframe.
		* SCAYT stops working when CKEditor [Undo plugin](https://ckeditor.com/cke4/addon/undo) not enabled.
		* Issue with pasting SCAYT markup in CKEditor.
		* SCAYT stops working after pressing the *Cancel* button in the WSC dialog.

## CKEditor 4.5.5

Fixed Issues:

* [#13887](https://dev.ckeditor.com/ticket/13887): Fixed: [Link](https://ckeditor.com/cke4/addon/link) plugin alters the `target` attribute value. Thanks to [SamZiemer](https://github.com/SamZiemer)!
* [#12189](https://dev.ckeditor.com/ticket/12189): Fixed: The [Link](https://ckeditor.com/cke4/addon/link) plugin dialog does not display the subject of email links if the subject parameter is not lowercase.
* [#9192](https://dev.ckeditor.com/ticket/9192): Fixed: An `undefined` string is appended to an email address added with the [Link](https://ckeditor.com/cke4/addon/link) plugin if subject and email body are empty and [`config.emailProtection`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-emailProtection) is set to `encode`.
* [#13790](https://dev.ckeditor.com/ticket/13790): Fixed: It is not possible to destroy the editor `<iframe>` after the editor was detached from DOM. Thanks to [Stefan Rijnhart](https://github.com/StefanRijnhart)!
* [#13803](https://dev.ckeditor.com/ticket/13803): Fixed: The editor cannot be destroyed before being fully initialized. Thanks to [Cyril Fluck](https://github.com/cyril-sf)!
* [#13867](https://dev.ckeditor.com/ticket/13867): Fixed: CKEditor does not work when the `classList` polyfill is used.
* [#13885](https://dev.ckeditor.com/ticket/13885): Fixed: [Enhanced Image](https://ckeditor.com/cke4/addon/image2) requires the [Link](https://ckeditor.com/cke4/addon/link) plugin to link an image.
* [#13883](https://dev.ckeditor.com/ticket/13883): Fixed: Copying a table using the context menu strips off styles.
* [#13872](https://dev.ckeditor.com/ticket/13872): Fixed: Cutting is possible in the [read-only](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-property-readOnly) mode.
* [#12848](https://dev.ckeditor.com/ticket/12848): [Blink] Fixed: Opening the [Find and Replace](https://ckeditor.com/cke4/addon/find) dialog window in the [read-only](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-property-readOnly) mode throws an exception.
* [#13879](https://dev.ckeditor.com/ticket/13879): Fixed: It is not possible to prevent the [`editor.drop`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-drop) event.
* [#13361](https://dev.ckeditor.com/ticket/13361): Fixed: Skin images fail when the site path includes parentheses because the `background-image` path needs single quotes around the URL value.
* [#13771](https://dev.ckeditor.com/ticket/13771): Fixed: The `contents.css` style is not used if the [IFrame Editing Area](https://ckeditor.com/cke4/addon/wysiwygarea) plugin is missing.
* [#13782](https://dev.ckeditor.com/ticket/13782): Fixed: Unclear log messages.
* [#13919](https://dev.ckeditor.com/ticket/13919): [Edge] Fixed: Browser window crashes when accessing the `isContentEditable` property of an `<input>` DOM element.

Other Changes:

* [#13859](https://dev.ckeditor.com/ticket/13859): Test cases created with `bender.tools.createTestsForEditors` will also receive editor bot as a second parameter.

## CKEditor 4.5.4

New Features:

* [#13632](https://dev.ckeditor.com/ticket/13632): Introduce error logging mechanism.
* [#13730](https://dev.ckeditor.com/ticket/13730): Switch to the new error logging mechanism.

Fixed Issues:

* [#9856](https://dev.ckeditor.com/ticket/9856): Fixed: Cannot use the native context menu together with the [Div Editing Area](https://ckeditor.com/cke4/addon/divarea) plugin. Thanks to [Mark Wade](https://github.com/mark-wade)!
* [#12733](https://dev.ckeditor.com/ticket/12733): [IE9+] Fixed: Radio button `onChange` does not work. Thanks to [Iliya Kostadinov](https://github.com/iliyakostadinov)!
* [#13142](https://dev.ckeditor.com/ticket/13142): [Edge] Fixed: *Ctrl+A* and then *Backspace* result in an empty `<div>` element.
* [#13599](https://dev.ckeditor.com/ticket/13599): Fixed: Cross-editor drag and drop of an inline widget results in error/artifacts.
* [#13640](https://dev.ckeditor.com/ticket/13640): [IE] Fixed: Dropping a widget outside the `<body>` element is not handled correctly.
* [#13533](https://dev.ckeditor.com/ticket/13533): Fixed: No progress during upload.
* [#13680](https://dev.ckeditor.com/ticket/13680): Fixed: The parser should allow the `<h1-6>` element to be a child of the `<summary>` element.
* [#11724](https://dev.ckeditor.com/ticket/11724): [Touch devices] Fixed: Drop-downs often hide right after opening them.
* [#13690](https://dev.ckeditor.com/ticket/13690): Fixed: Copying content from IE to Chrome adds an extra paragraph.
* [#13284](https://dev.ckeditor.com/ticket/13284): Fixed: Cannot drag and drop a widget if the text caret is placed just after the widget instance.
* [#13516](https://dev.ckeditor.com/ticket/13516): Fixed: CKEditor removes empty HTML5 anchors without the `name` attribute.
* [#13765](https://dev.ckeditor.com/ticket/13765): [Safari 9] Fixed: Problems with rendering samples.

Other Changes:

* [#11725](https://dev.ckeditor.com/ticket/11725): Marked [`CKEDITOR.env.mobile`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.env-property-mobile) as deprecated. The reason is that it is no longer clear what "mobile" means.
* [#13737](https://dev.ckeditor.com/ticket/13737): Upgraded [Bender.js](https://github.com/benderjs/benderjs) to 0.4.1.

## CKEditor 4.5.3

New Features:

* [#13501](https://dev.ckeditor.com/ticket/13501): Added the [`config.fileTools_defaultFileName`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-fileTools_defaultFileName) option to allow setting a default file name for paste uploads.
* [#13603](https://dev.ckeditor.com/ticket/13603): Added support for uploading dropped BMP images.

Fixed Issues:

* [#13590](https://dev.ckeditor.com/ticket/13590): Fixed: Various issues related to the [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) feature. Fixes also:
  * [#11215](https://dev.ckeditor.com/ticket/11215),
  * [#8780](https://dev.ckeditor.com/ticket/8780),
  * [#12762](https://dev.ckeditor.com/ticket/12762).
* [#13386](https://dev.ckeditor.com/ticket/13386): [Edge] Fixed: Issues with selecting and editing images.
* [#13568](https://dev.ckeditor.com/ticket/13568): Fixed: The [`editor.getSelectedHtml()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getSelectedHtml) method returns invalid results for entire content selection.
* [#13453](https://dev.ckeditor.com/ticket/13453): Fixed: Drag&drop of entire editor content throws an error.
* [#13465](https://dev.ckeditor.com/ticket/13465): Fixed: Error is thrown and the widget is lost on drag&drop if it is the only content of the editor.
* [#13414](https://dev.ckeditor.com/ticket/13414): Fixed: Content auto paragraphing in a nested editable despite editor configuration.
* [#13429](https://dev.ckeditor.com/ticket/13429): Fixed: Incorrect selection after content insertion by the [Auto Embed](https://ckeditor.com/cke4/addon/autoembed) plugin.
* [#13388](https://dev.ckeditor.com/ticket/13388): Fixed: [Table Resize](https://ckeditor.com/cke4/addon/tableresize) integration with [Undo](https://ckeditor.com/cke4/addon/undo) is broken.

Other Changes:

* [#13637](https://dev.ckeditor.com/ticket/13637): Several icons were refactored.
* Updated [Bender.js](https://github.com/benderjs/benderjs) to 0.3.0 and introduced the ability to run tests via HTTPs ([#13265](https://dev.ckeditor.com/ticket/13265)).

## CKEditor 4.5.2

Fixed Issues:

* [#13609](https://dev.ckeditor.com/ticket/13609): [Edge] Fixed: The browser crashes when switching to the source mode. Thanks to [Andrew Williams and Mark Smeed](http://webxsolution.com/)!
* [PR#201](https://github.com/ckeditor/ckeditor-dev/pull/201): Fixed: Buttons in the toolbar configurator cause form submission. Thanks to [colemanw](https://github.com/colemanw)!
* [#13422](https://dev.ckeditor.com/ticket/13422): Fixed: A monospaced font should be used in the `<textarea>` element storing editor configuration in the toolbar configurator.
* [#13494](https://dev.ckeditor.com/ticket/13494): Fixed: Error thrown in the toolbar configurator if plugin requirements are not met.
* [#13409](https://dev.ckeditor.com/ticket/13409): Fixed: List elements incorrectly merged when pressing *Backspace* or *Delete*.
* [#13434](https://dev.ckeditor.com/ticket/13434): Fixed: Dialog state indicator broken in Right–To–Left environments.
* [#13460](https://dev.ckeditor.com/ticket/13460): [IE8] Fixed: Copying inline widgets is broken when [Advanced Content Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_acf) is disabled.
* [#13495](https://dev.ckeditor.com/ticket/13495): [Firefox, IE] Fixed: Text is not word-wrapped in the Paste dialog window.
* [#13528](https://dev.ckeditor.com/ticket/13528): [Firefox@Windows] Fixed: Content copied from Microsoft Word and other external applications is pasted as a plain text. Removed the `CKEDITOR.plugins.clipboard.isHtmlInExternalDataTransfer` property as the check must be dynamic.
* [#13583](https://dev.ckeditor.com/ticket/13583): Fixed: [`DataTransfer.getData()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.clipboard.dataTransfer-method-getData) should work consistently in all browsers and should not strip valuable content. Fixed pasting tables from Microsoft Excel on Chrome.
* [#13468](https://dev.ckeditor.com/ticket/13468): [IE] Fixed: Binding drag&drop `dataTransfer` does not work if `text` data was set in the meantime.
* [#13451](https://dev.ckeditor.com/ticket/13451): [IE8-9] Fixed: One drag&drop operation may affect following ones.
* [#13184](https://dev.ckeditor.com/ticket/13184): Fixed: Web page reloaded after a drop on editor UI.
* [#13129](https://dev.ckeditor.com/ticket/13129) Fixed: Block widget blurred after a drop followed by an undo.
* [#13397](https://dev.ckeditor.com/ticket/13397): Fixed: Drag&drop of a widget inside its nested widget crashes the editor.
* [#13385](https://dev.ckeditor.com/ticket/13385): Fixed: [`editor.getSnapshot()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getSnapshot) may return a non-string value.
* [#13419](https://dev.ckeditor.com/ticket/13419): Fixed: The [Auto Link](https://ckeditor.com/cke4/addon/autolink) plugin does not encode double quotes in URLs.
* [#13420](https://dev.ckeditor.com/ticket/13420): Fixed: The [Auto Embed](https://ckeditor.com/cke4/addon/autoembed) plugin ignores encoded characters in URL parameters.
* [#13410](https://dev.ckeditor.com/ticket/13410): Fixed: Error thrown in the [Auto Embed](https://ckeditor.com/cke4/addon/autoembed) plugin when undoing right after pasting a link.
* [#13566](https://dev.ckeditor.com/ticket/13566): Fixed: Suppressed notifications in the [Media Embed Base](https://ckeditor.com/cke4/addon/embedbase) plugin.
* [#11616](https://dev.ckeditor.com/ticket/11616): [Chrome] Fixed: Resizing the editor while it is not displayed breaks the editable. Fixes also [#9160](https://dev.ckeditor.com/ticket/9160) and [#9715](https://dev.ckeditor.com/ticket/9715).
* [#11376](https://dev.ckeditor.com/ticket/11376): [IE11] Fixed: Loss of text when pasting bulleted lists from Microsoft Word.
* [#13143](https://dev.ckeditor.com/ticket/13143): [Edge] Fixed: Focus lost when opening the panel.
* [#13387](https://dev.ckeditor.com/ticket/13387): [Edge] Fixed: "Permission denied" error thrown when loading the editor with developer tools open.
* [#13574](https://dev.ckeditor.com/ticket/13574): [Edge] Fixed: "Permission denied" error thrown when opening editor dialog windows.
* [#13441](https://dev.ckeditor.com/ticket/13441): [Edge] Fixed: The [Clipboard](https://ckeditor.com/cke4/addon/clipboard) plugin breaks the state of [Undo](https://ckeditor.com/cke4/addon/undo) commands after a paste.
* [#13554](https://dev.ckeditor.com/ticket/13554): [Edge] Fixed: Paste dialog's iframe does not receive focus on show.
* [#13440](https://dev.ckeditor.com/ticket/13440): [Edge] Fixed: Unable to paste a widget.

Other Changes:

* [#13421](https://dev.ckeditor.com/ticket/13421): UX improvements to notifications in the [Auto Embed](https://ckeditor.com/cke4/addon/autoembed) plugin.

## CKEditor 4.5.1

Fixed Issues:

* [#13486](https://dev.ckeditor.com/ticket/13486): Fixed: The [Upload Image](https://ckeditor.com/cke4/addon/uploadimage) plugin should log an error, not throw an error when upload URL is not set.

## CKEditor 4.5

New Features:

* [#13304](https://dev.ckeditor.com/ticket/13304): Added support for passing DOM elements to [`config.sharedSpaces`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-sharedSpaces). Thanks to [Undergrounder](https://github.com/Undergrounder)!
* [#13215](https://dev.ckeditor.com/ticket/13215): Added ability to cancel fetching a resource by the Embed plugins.
* [#13213](https://dev.ckeditor.com/ticket/13213): Added the [`dialog#setState()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dialog-method-setState) method and used it in the [Embed](https://ckeditor.com/cke4/addon/embed) dialog to indicate that a resource is being loaded.
* [#13337](https://dev.ckeditor.com/ticket/13337): Added the [`repository.onWidget()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget.repository-method-onWidget) method &mdash; a convenient way to listen to [widget](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget) events through the [repository](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget.repository).
* [#13214](https://dev.ckeditor.com/ticket/13214): Added support for pasting links that convert into embeddable resources on the fly.

Fixed Issues:

* [#13334](https://dev.ckeditor.com/ticket/13334): Fixed: Error after nesting widgets and playing with undo/redo.
* [#13118](https://dev.ckeditor.com/ticket/13118): Fixed: The [`editor.getSelectedHtml()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getSelectedHtml) method throws an error when called in the source mode.
* [#13158](https://dev.ckeditor.com/ticket/13158): Fixed: Error after canceling a dialog when creating a widget.
* [#13197](https://dev.ckeditor.com/ticket/13197): Fixed: Linked inline [Enhanced Image](https://ckeditor.com/cke4/addon/image2) alignment class is not transferred to the widget wrapper.
* [#13199](https://dev.ckeditor.com/ticket/13199): Fixed: [Semantic Embed](https://ckeditor.com/cke4/addon/embedsemantic) does not support widget classes.
* [#13003](https://dev.ckeditor.com/ticket/13003): Fixed: Anchors are uploaded when moving them by drag and drop.
* [#13032](https://dev.ckeditor.com/ticket/13032): Fixed: When upload is done, notification update should be marked as important.
* [#13300](https://dev.ckeditor.com/ticket/13300): Fixed: The `internalCommit` argument in the [Image](https://ckeditor.com/cke4/addon/image) dialog seems to be never used.
* [#13036](https://dev.ckeditor.com/ticket/13036): Fixed: Notifications are moved 10px to the right.
* [#13280](https://dev.ckeditor.com/ticket/13280): [IE8] Fixed: Undo after inline widget drag&drop throws an error.
* [#13186](https://dev.ckeditor.com/ticket/13186): Fixed: Content dropped into a nested editable is not filtered by [Advanced Content Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_acf).
* [#13140](https://dev.ckeditor.com/ticket/13140): Fixed: Error thrown when dropping a block widget right after itself.
* [#13176](https://dev.ckeditor.com/ticket/13176): [IE8] Fixed: Errors on drag&drop of embed widgets.
* [#13015](https://dev.ckeditor.com/ticket/13015): Fixed: Dropping an image file on [Enhanced Image](https://ckeditor.com/cke4/addon/image2) causes a page reload.
* [#13080](https://dev.ckeditor.com/ticket/13080): Fixed: Ugly notification shown when the response contains HTML content.
* [#13011](https://dev.ckeditor.com/ticket/13011): [IE8] Fixed: Anchors are duplicated on drag&drop in specific locations.
* [#13105](https://dev.ckeditor.com/ticket/13105): Fixed: Various issues related to [`CKEDITOR.tools.htmlEncode()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools-method-htmlEncode) and [`CKEDITOR.tools.htmlDecode()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.tools-method-htmlDecode) methods.
* [#11976](https://dev.ckeditor.com/ticket/11976): [Chrome] Fixed: Copy&paste and drag&drop lists from Microsoft Word.
* [#13128](https://dev.ckeditor.com/ticket/13128): Fixed: Various issues with cloning element IDs:
  * Fixed the default behavior of [`range.cloneContents()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.range-method-cloneContents) and [`range.extractContents()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.range-method-extractContents) methods which now clone IDs similarly to their native counterparts.
  * Added `cloneId` arguments to the above methods, [`range.splitBlock()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.range-method-splitBlock) and [`element.breakParent()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-breakParent). Mind the default values and special behavior in the `extractContents()` method!
  * Fixed issues where IDs were lost on copy&paste and drag&drop.
* Toolbar configurators:
  * [#13185](https://dev.ckeditor.com/ticket/13185): Fixed: Wrong position of the suggestion box if there is not enough space below the caret.
  * [#13138](https://dev.ckeditor.com/ticket/13138): Fixed: The "Toggle empty elements" button label is unclear.
  * [#13136](https://dev.ckeditor.com/ticket/13136): Fixed: Autocompleter is far too intrusive.
  * [#13133](https://dev.ckeditor.com/ticket/13133): Fixed: Tab leaves the editor.
  * [#13173](https://dev.ckeditor.com/ticket/13173): Fixed: [`config.removeButtons`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-removeButtons) is ignored by the advanced toolbar configurator.

Other Changes:

* [#13119](https://dev.ckeditor.com/ticket/13119): Improved compatibility of editor skins ([Moono](https://ckeditor.com/cke4/addon/moono) and [Kama](https://ckeditor.com/cke4/addon/kama)) with external web page style sheets.
* Toolbar configurators:
  * [#13147](https://dev.ckeditor.com/ticket/13147): Added buttons to the sticky toolbar.
  * [#13207](https://dev.ckeditor.com/ticket/13207): Used modal window to display toolbar configurator help.
* [#13316](https://dev.ckeditor.com/ticket/13316): Made [`CKEDITOR.env.isCompatible`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.env-property-isCompatible) a blacklist rather than a whitelist. More about the change in the [Browser Compatibility](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_browsers) guide.
* [#13398](https://dev.ckeditor.com/ticket/13398): Renamed `CKEDITOR.fileTools.UploadsRepository` to [`CKEDITOR.fileTools.UploadRepository`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.fileTools.uploadRepository) and changed all related properties.
* [#13279](https://dev.ckeditor.com/ticket/13279): Reviewed CSS vendor prefixes.
* [#13454](https://dev.ckeditor.com/ticket/13454): Removed unused `lang.image.alertUrl` token from the [Image](https://ckeditor.com/cke4/addon/image) plugin.

## CKEditor 4.5 Beta

New Features:

* Clipboard (copy&paste, drag&drop) and file uploading features and improvements ([#11437](https://dev.ckeditor.com/ticket/11437)).

  * Major features:
    * Support for dropping and pasting files into the editor was introduced. Through a set of new facades for native APIs it is now possible to easily intercept and process inserted files.
    * [File upload tools](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.fileTools) were introduced in order to simplify controlling the loading, uploading and handling server response, properly handle [new upload configuration](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-uploadUrl) options, etc.
    * [Upload Image](https://ckeditor.com/cke4/addon/uploadimage) widget was introduced to upload dropped images. A base class for the [upload widget](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.fileTools.uploadWidgetDefinition) was exposed, too, to make it simple to create new types of upload widgets which can handle any type of dropped file, show the upload progress and update the content when the process is done. It also handles editing and undo/redo operations when a file is being uploaded and integrates with the [notification aggregator](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.notificationAggregator) to show progress and success or error.
    * All drag and drop operations were integrated with the editor. All dropped content is passed through the [`editor#paste`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-paste) event and a set of new editor events was introduced &mdash; [`dragstart`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-dragstart), [`drop`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-drop), [`dragend`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-dragend).
    * The [Data Transfer](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.clipboard.dataTransfer) facade was introduced to unify access to data in various types and files. [Data Transfer](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.clipboard.dataTransfer) is now always available in the [`editor#paste`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-paste) event.
    * Switched from the pastebin to using the native clipboard access whenever possible. This solved many issues related to pastebin such as unnecessary scrolling or data loss. Additionally, on copy and cut from the editor the clipboard data is set. Therefore, on paste the editor has access to clean data, undisturbed by the browsers.
    * Drag and drop of inline and block widgets was integrated with the standard clipboard APIs. By listening to drag events you will thus be notified about widgets, too. This opens a possibility to filter pasted and dropped widgets.
    * The [`editor#paste`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-paste) event can have the `range` parameter so it is possible to change the paste position in the listener or paste in the not selectable position. Also the [`editor.insertHtml()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-insertHtml) method now accepts `range` as an additional parameter.
    * [#11621](https://dev.ckeditor.com/ticket/11621): A configurable [paste filter](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-pasteFilter) was introduced. The filter is by default turned to `'semantic-content'` on Webkit and Blink for all pasted content coming from external sources because of the low quality of HTML that these engines put into the clipboard. Internal and cross-editor paste is safe due to the change explained in the previous point.

  * Other changes and related fixes:
    * [#12095](https://dev.ckeditor.com/ticket/12095): On drag and copy of widgets [the same method](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getSelectedHtml) is used to get selected HTML as in the normal case. Thanks to that styles applied to inline widgets are not lost.
    * [#11219](https://dev.ckeditor.com/ticket/11219): Fixed: Dragging a [captioned image](https://ckeditor.com/cke4/addon/image2) does not fire the [`editor#paste`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-paste) event.
    * [#9554](https://dev.ckeditor.com/ticket/9554): [Webkit Mac] Fixed: Editor scrolls on paste.
    * [#9898](https://dev.ckeditor.com/ticket/9898): [Webkit&Divarea] Fixed: Pasting causes undesirable scrolling.
    * [#11993](https://dev.ckeditor.com/ticket/11993): [Chrome] Fixed: Pasting content scrolls the document.
    * [#12613](https://dev.ckeditor.com/ticket/12613): Show the user that they can not drop on editor UI (toolbar, bottom bar).
    * [#12851](https://dev.ckeditor.com/ticket/12851): [Blink/Webkit] Fixed: Formatting disappears when pasting content into cells.
    * [#12914](https://dev.ckeditor.com/ticket/12914): Fixed: Copy/Paste of table broken in `div`-based editor.

  * Browser support.<br>Browser support for related features varies significantly (see http://caniuse.com/clipboard).
    * File APIs needed to operate and file upload is not supported in Internet Explorer 9 and below.
    * Only Chrome and Safari on Mac OS support setting custom data items in the clipboard, so currently it is possible to recognize the origin of the copied content in these browsers only. All drag and drop operations can be identified thanks to the new Data Transfer facade.
    * No Internet Explorer browser supports the standard clipboard API which results in small glitches like where only plain text can be dropped from outside the editor. Thanks to the new Data Transfer facade, internal and cross-editor drag and drop supports the full range of data.
    * Direct access to clipboard could only be implemented in Chrome, Safari on Mac OS, Opera and Firefox. In other browsers the pastebin must still be used.

* [#12875](https://dev.ckeditor.com/ticket/12875): Samples and toolbar configuration tools.
  * The old set of samples shipped with every CKEditor package was replaced with a shiny new single-page sample. This change concluded a long term plan which started from introducing the [CKEditor SDK](https://sdk.ckeditor.com/) and [CKEditor Functionality Overview](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_features) section in the documentation which essentially redefined the old samples.
  * Toolbar configurators with live previews were introduced. They will be shipped with every CKEditor package and are meant to help in configuring toolbar layouts.

* [#10925](https://dev.ckeditor.com/ticket/10925): The [Media Embed](https://ckeditor.com/cke4/addon/embed) and [Semantic Media Embed](https://ckeditor.com/cke4/addon/embedsemantic) plugins were introduced. Read more about the new features in the [Embedding Content](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_media_embed) article.
* [#10931](https://dev.ckeditor.com/ticket/10931): Added support for nesting widgets. It is now possible to insert one widget into another widget's nested editable. Note that unless nested editable's [allowed content](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget.nestedEditable.definition-property-allowedContent) is defined precisely, starting from CKEditor 4.5 some widget buttons may become enabled. This feature is not supported in IE8. Included issues:
  * [#12018](https://dev.ckeditor.com/ticket/12018): Fixed and reviewed: Nested widgets garbage collection.
  * [#12024](https://dev.ckeditor.com/ticket/12024): [Firefox] Fixed: Outline is extended to the left by unpositioned drag handlers.
  * [#12006](https://dev.ckeditor.com/ticket/12006): Fixed: Drag and drop of nested block widgets.
  * [#12008](https://dev.ckeditor.com/ticket/12008): Fixed various cases of inserting a single non-editable element using the [`editor.insertHtml()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-insertHtml) method. Fixes pasting a widget with a nested editable inside another widget's nested editable.

* Notification system:
  * [#11580](https://dev.ckeditor.com/ticket/11580): Introduced the [notification system](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.notification).
  * [#12810](https://dev.ckeditor.com/ticket/12810): Introduced a [notification aggregator](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.notificationAggregator) for the [notification system](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.notification) which simplifies displaying progress of many concurrent tasks.
* [#11636](https://dev.ckeditor.com/ticket/11636): Introduced new, UX-focused, methods for getting selected HTML and deleting it &mdash; [`editor.getSelectedHtml()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getSelectedHtml) and [`editor.extractSelectedHtml()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-extractSelectedHtml).
* [#12416](https://dev.ckeditor.com/ticket/12416): Added the [`widget.definition.upcastPriority`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget.definition-property-upcastPriority) property which gives more control over widget upcasting order to the widget author.
* [#12036](https://dev.ckeditor.com/ticket/12036): Initialize the editor in [read-only](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-property-readOnly) mode when the `<textarea>` element has a `readonly` attribute.
* [#11905](https://dev.ckeditor.com/ticket/11905): The [`resize` event](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-resize) passes the current dimensions in its data.
* [#12126](https://dev.ckeditor.com/ticket/12126): Introduced [`config.image_prefillDimensions`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-image_prefillDimensions) and [`config.image2_prefillDimensions`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-image2_prefillDimensions) to make pre-filling `width` and `height` configurable for the [Enhanced Image](https://ckeditor.com/cke4/addon/image2).
* [#12746](https://dev.ckeditor.com/ticket/12746): Added a new configuration option to hide the [Enhanced Image](https://ckeditor.com/cke4/addon/image2) resizer.
* [#12150](https://dev.ckeditor.com/ticket/12150): Exposed the [`getNestedEditable()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget-static-method-getNestedEditable) and `is*` [widget helper](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget) functions (see the static methods).
* [#12448](https://dev.ckeditor.com/ticket/12448): Introduced the [`editable.insertHtmlIntoRange`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editable-method-insertHtmlIntoRange) method.
* [#12143](https://dev.ckeditor.com/ticket/12143): Added the [`config.floatSpacePreferRight`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-floatSpacePreferRight) configuration option that switches the alignment of the floating toolbar. Thanks to [InvisibleBacon](http://github.com/InvisibleBacon)!
* [#10986](https://dev.ckeditor.com/ticket/10986): Added support for changing dialog input and textarea text directions by using the *Shift+Alt+Home/End* keystrokes. The direction is stored in the value of the input by prepending the [`\u202A`](http://unicode.org/cldr/utility/character.jsp?a=202A) or [`\u202B`](http://unicode.org/cldr/utility/character.jsp?a=202B) marker to it. Read more in the [documentation](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dialog.definition.textInput-property-bidi). Thanks to [edithkk](https://github.com/edithkk)!
* [#12770](https://dev.ckeditor.com/ticket/12770): Added support for passing [widget](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget)'s startup data as a widget command's argument. Thanks to [Rebrov Boris](https://github.com/zipp3r) and [Tieme van Veen](https://github.com/tiemevanveen)!
* [#11583](https://dev.ckeditor.com/ticket/11583): Added support for the HTML5 `required` attribute in various form elements. Thanks to [Steven Busse](https://github.com/sbusse)!

Changes:

* [#12858](https://dev.ckeditor.com/ticket/12858): Basic [Spartan](http://blogs.windows.com/bloggingwindows/2015/03/30/introducing-project-spartan-the-new-browser-built-for-windows-10/) browser compatibility. Full compatibility will be introduced later, because at the moment Spartan is still too unstable to be used for tests and we see many changes from version to version.
* [#12948](https://dev.ckeditor.com/ticket/12948): The [`config.mathJaxLibrary`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-mathJaxLib) option does not default to the MathJax CDN any more. It needs to be configured to enable the [Mathematical Formulas](https://ckeditor.com/cke4/addon/mathjax) plugin now.
* [#13069](https://dev.ckeditor.com/ticket/13069): Fixed inconsistencies between [`editable.insertHtml()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editable-method-insertElement) and [`editable.insertElement()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editable-method-insertElement) when the `range` parameter is used. Now, the `editor.insertElement()` method works on a higher level, which means that it saves undo snapshots and sets the selection after insertion. Use the [`editable.insertElementIntoRange()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editable-method-insertElementIntoRange) method directly for the pre 4.5 behavior of `editable.insertElement()`.
* [#12870](https://dev.ckeditor.com/ticket/12870): Use [`editor.showNotification()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-showNotification) instead of `alert()` directly whenever possible. When the [Notification plugin](https://ckeditor.com/cke4/addon/notification) is loaded, the notification system is used automatically. Otherwise, the native `alert()` is displayed.
* [#8024](https://dev.ckeditor.com/ticket/8024): Swapped behavior of the Split Cell Vertically and Horizontally features of the [Table Tools](https://ckeditor.com/cke4/addon/tabletools) plugin to be more intuitive. Thanks to [kevinisagit](https://github.com/kevinisagit)!
* [#10903](https://dev.ckeditor.com/ticket/10903): Performance improvements for the [`dom.element.addClass()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-addClass), [`dom.element.removeClass()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-removeClass) and [`dom.element.hasClass()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-hasClass) methods. Note: The previous implementation allowed passing multiple classes to `addClass()` although it was only a side effect of that implementation. The new implementation does not allow this.
* [#11856](https://dev.ckeditor.com/ticket/11856): The jQuery adapter throws a meaningful error if CKEditor or jQuery are not loaded.

Fixed issues:

* [#11586](https://dev.ckeditor.com/ticket/11586): Fixed: [`range.cloneContents()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.range-method-cloneContents) should not change the DOM in order not to affect selection.
* [#12148](https://dev.ckeditor.com/ticket/12148): Fixed: [`dom.element.getChild()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-getChild) should not modify a passed array.
* [#12503](https://dev.ckeditor.com/ticket/12503): [Blink/Webkit] Fixed: Incorrect result of Select All and *Backspace* or *Delete*.
* [#13001](https://dev.ckeditor.com/ticket/13001): [Firefox] Fixed: The `<br />` filler is placed in the wrong position by the [`range.fixBlock()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.range-method-fixBlock) method due to quirky Firefox behavior.
* [#13101](https://dev.ckeditor.com/ticket/13101): [IE8] Fixed: Colons are prepended to HTML5 element names when cloning them.

## CKEditor 4.4.8

**Security Updates:**

* Fixed XSS vulnerability in the HTML parser reported by [Dheeraj Joshi](https://twitter.com/dheerajhere) and [Prem Kumar](https://twitter.com/iAmPr3m).

	Issue summary: It was possible to execute XSS inside CKEditor after persuading the victim to: (i) switch CKEditor to source mode, then (ii) paste a specially crafted HTML code, prepared by the attacker, into the opened CKEditor source area, and (iii) switch back to WYSIWYG mode.

**An upgrade is highly recommended!**

Fixed Issues:

* [#12899](https://dev.ckeditor.com/ticket/12899): Fixed: Corrected wrong tag ending for horizontal box definition in the [Dialog User Interface](https://ckeditor.com/cke4/addon/dialogui) plugin. Thanks to [mizafish](https://github.com/mizafish)!
* [#13254](https://dev.ckeditor.com/ticket/13254): Fixed: Cannot outdent block after indent when using the [Div Editing Area](https://ckeditor.com/cke4/addon/divarea) plugin. Thanks to [Jonathan Cottrill](https://github.com/jcttrll)!
* [#13268](https://dev.ckeditor.com/ticket/13268): Fixed: Documentation for [`CKEDITOR.dom.text`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.text) is incorrect. Thanks to [Ben Kiefer](https://github.com/benkiefer)!
* [#12739](https://dev.ckeditor.com/ticket/12739): Fixed: Link loses inline styles when edited without the [Advanced Tab for Dialogs](https://ckeditor.com/cke4/addon/dialogadvtab) plugin. Thanks to [Віталій Крутько](https://github.com/asmforce)!
* [#13292](https://dev.ckeditor.com/ticket/13292): Fixed: Protection pattern does not work in attribute in self-closing elements with no space before `/>`. Thanks to [Віталій Крутько](https://github.com/asmforce)!
* [PR#192](https://github.com/ckeditor/ckeditor-dev/pull/192): Fixed: Variable name typo in the [Dialog User Interface](https://ckeditor.com/cke4/addon/dialogui) plugin which caused [`CKEDITOR.ui.dialog.radio`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.ui.dialog.radio) validation to not work. Thanks to [Florian Ludwig](https://github.com/FlorianLudwig)!
* [#13232](https://dev.ckeditor.com/ticket/13232): [Safari] Fixed: The [`element.appendText()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-appendText) method does not work properly for empty elements.
* [#13233](https://dev.ckeditor.com/ticket/13233): Fixed: [HTMLDataProcessor](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.htmlDataProcessor) can process `foo:href` attributes.
* [#12796](https://dev.ckeditor.com/ticket/12796): Fixed: The [Indent List](https://ckeditor.com/cke4/addon/indentlist) plugin unwraps parent `<li>` elements. Thanks to [Andrew Stucki](https://github.com/andrewstucki)!
* [#12885](https://dev.ckeditor.com/ticket/12885): Added missing [`editor.getData()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-getData) parameter documentation.
* [#11982](https://dev.ckeditor.com/ticket/11982): Fixed: Bullet added in a wrong position after the *Enter* key is pressed in a nested list.
* [#13027](https://dev.ckeditor.com/ticket/13027): Fixed: Keyboard navigation in dialog windows with multiple tabs not following IBM CI 162 instructions or [ARIA Authoring Practices](http://www.w3.org/TR/2013/WD-wai-aria-practices-20130307/#tabpanel).
* [#12256](https://dev.ckeditor.com/ticket/12256): Fixed: Basic styles classes are lost when pasting from Microsoft Word if [basic styles](https://ckeditor.com/cke4/addon/basicstyles) were configured to use classes.
* [#12729](https://dev.ckeditor.com/ticket/12729): Fixed: Incorrect structure created when merging a block into a list item on *Backspace* and *Delete*.
* [#13031](https://dev.ckeditor.com/ticket/13031): [Firefox] Fixed: No more line breaks in source view since Firefox 36.
* [#13131](https://dev.ckeditor.com/ticket/13131): Fixed: The [Code Snippet](https://ckeditor.com/cke4/addon/codesnippet) plugin cannot be used without the [IFrame Editing Area](https://ckeditor.com/cke4/addon/wysiwygarea) plugin.
* [#9086](https://dev.ckeditor.com/ticket/9086): Fixed: Invalid ARIA property used on paste area `<iframe>`.
* [#13164](https://dev.ckeditor.com/ticket/13164): Fixed: Error when inserting a hidden field.
* [#13155](https://dev.ckeditor.com/ticket/13155): Fixed: Incorrect [Line Utilities](https://ckeditor.com/cke4/addon/lineutils) positioning when `<body>` has a margin.
* [#13351](https://dev.ckeditor.com/ticket/13351): Fixed: Link lost when editing a linked image with the Link tab disabled. This also fixed a bug when inserting an image into a fully selected link would throw an error ([#12847](https://dev.ckeditor.com/ticket/12847)).
* [#13344](https://dev.ckeditor.com/ticket/13344): [WebKit/Blink] Fixed: It is possible to remove or change editor content in [read-only mode](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_readonly).

Other Changes:

* [#12844](https://dev.ckeditor.com/ticket/12844) and [#13103](https://dev.ckeditor.com/ticket/13103): Upgraded the [testing environment](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_tests) to [Bender.js](https://github.com/benderjs/benderjs) `0.2.3`.
* [#12930](https://dev.ckeditor.com/ticket/12930): Because of licensing issues, `truncated-mathjax/` is now removed from the `tests/` directory. Now `bender.config.mathJaxLibPath` must be configured manually in order to run [Mathematical Formulas](https://ckeditor.com/cke4/addon/mathjax) plugin tests.
* [#13266](https://dev.ckeditor.com/ticket/13266): Added more shades of gray in the [Color Dialog](https://ckeditor.com/cke4/addon/colordialog) window. Thanks to [mizafish](https://github.com/mizafish)!


## CKEditor 4.4.7

Fixed Issues:

* [#12825](https://dev.ckeditor.com/ticket/12825): Fixed: Preventing the [Table Resize](https://ckeditor.com/cke4/addon/tableresize) plugin from operating on elements outside the editor. Thanks to [Paul Martin](https://github.com/Paul-Martin)!
* [#12157](https://dev.ckeditor.com/ticket/12157): Fixed: Lost text formatting on pressing *Tab* when the [`config.tabSpaces`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-tabSpaces) configuration option value was greater than zero.
* [#12777](https://dev.ckeditor.com/ticket/12777): Fixed: The `table-layout` CSS property should be reset by skins. Thanks to [vita10gy](https://github.com/vita10gy)!
* [#12812](https://dev.ckeditor.com/ticket/12812): Fixed: An uncaught security exception is thrown when [Line Utilities](https://ckeditor.com/cke4/addon/lineutils) are used in an inline editor loaded in a cross-domain `iframe`. Thanks to [Vitaliy Zurian](https://github.com/thecatontheflat)!
* [#12735](https://dev.ckeditor.com/ticket/12735): Fixed: [`config.fillEmptyBlocks`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-fillEmptyBlocks) should only apply when outputting data.
* [#10032](https://dev.ckeditor.com/ticket/10032): Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) filter is executed for every paste after using the button.
* [#12597](https://dev.ckeditor.com/ticket/12597): [Blink/WebKit] Fixed: Multi-byte Japanese characters entry not working properly after *Shift+Enter*.
* [#12387](https://dev.ckeditor.com/ticket/12387): Fixed: An error is thrown if a skin does not have the [`chameleon`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.skin-method-chameleon) property defined and [`config.uiColor`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-uiColor) is defined.
* [#12747](https://dev.ckeditor.com/ticket/12747): [IE8-10] Fixed: Opening a drop-down for a specific selection when the editor is maximized results in incorrect drop-down panel position.
* [#12850](https://dev.ckeditor.com/ticket/12850): [IEQM] Fixed: An error is thrown after focusing the editor.

## CKEditor 4.4.6

**Security Updates:**

* Fixed XSS vulnerability in the HTML parser reported by [Maco Cortes](https://www.facebook.com/Maaacoooo).

	Issue summary: It was possible to execute XSS inside CKEditor after persuading the victim to: (i) switch CKEditor to source mode, then (ii) paste a specially crafted HTML code, prepared by the attacker, into the opened CKEditor source area, and (iii) switch back to WYSIWYG mode.

**An upgrade is highly recommended!**

New Features:

* [#12501](https://dev.ckeditor.com/ticket/12501): Allowed dashes in element names in the [string format of allowed content rules](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_allowed_content_rules-section-string-format).
* [#12550](https://dev.ckeditor.com/ticket/12550): Added the `<main>` element to the [`CKEDITOR.dtd`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dtd).

Fixed Issues:

* [#12506](https://dev.ckeditor.com/ticket/12506): [Safari] Fixed: Cannot paste into inline editor if the page has `user-select: none` style. Thanks to [shaohua](https://github.com/shaohua)!
* [#12683](https://dev.ckeditor.com/ticket/12683): Fixed: [Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_acf) fails to remove custom tags. Thanks to [timselier](https://github.com/timselier)!
* [#12489](https://dev.ckeditor.com/ticket/12489) and [#12491](https://dev.ckeditor.com/ticket/12491): Fixed: Various issues related to restoring the selection after performing operations on filler character. See the [fixed cases](https://dev.ckeditor.com/ticket/12491#comment:4).
* [#12621](https://dev.ckeditor.com/ticket/12621): Fixed: Cannot remove inline styles (bold, italic, etc.) in empty lines.
* [#12630](https://dev.ckeditor.com/ticket/12630): [Chrome] Fixed: Selection is placed outside the paragraph when the [New Page](https://ckeditor.com/cke4/addon/newpage) button is clicked. This patch significantly simplified the way how the initial selection (a selection after the content of the editable is overwritten) is being fixed. That might have fixed many related scenarios in all browsers.
* [#11647](https://dev.ckeditor.com/ticket/11647): Fixed: The [`editor.blur`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-blur) event is not fired on first blur after initializing the inline editor on an already focused element.
* [#12601](https://dev.ckeditor.com/ticket/12601): Fixed: [Strikethrough](https://ckeditor.com/cke4/addon/basicstyles) button tooltip spelling.
* [#12546](https://dev.ckeditor.com/ticket/12546): Fixed: The Preview tab in the [Document Properties](https://ckeditor.com/cke4/addon/docprops) dialog window is always disabled.
* [#12300](https://dev.ckeditor.com/ticket/12300): Fixed: The [`editor.change`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-change) event fired on first navigation key press after typing.
* [#12141](https://dev.ckeditor.com/ticket/12141): Fixed: List items are lost when indenting a list item with content wrapped with a block element.
* [#12515](https://dev.ckeditor.com/ticket/12515): Fixed: Cursor is in the wrong position when undoing after adding an image and typing some text.
* [#12484](https://dev.ckeditor.com/ticket/12484): [Blink/WebKit] Fixed: DOM is changed outside the editor area in a certain case.
* [#12688](https://dev.ckeditor.com/ticket/12688): Improved the tests of the [styles system](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.style) and fixed two minor issues.
* [#12403](https://dev.ckeditor.com/ticket/12403): Fixed: Changing the [font](https://ckeditor.com/cke4/addon/font) style should not lead to nesting it in the previous style element.
* [#12609](https://dev.ckeditor.com/ticket/12609): Fixed: Incorrect `config.magicline_putEverywhere` name used for a [Magic Line](https://ckeditor.com/cke4/addon/magicline) all-encompassing [`config.magicline_everywhere`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-magicline_everywhere) configuration option.


## CKEditor 4.4.5

New Features:

* [#12279](https://dev.ckeditor.com/ticket/12279): Added a possibility to pass a custom evaluator to [`node.getAscendant()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.node-method-getAscendant).

Fixed Issues:

* [#12423](https://dev.ckeditor.com/ticket/12423): [Safari7.1+] Fixed: *Enter* key moved cursor to a strange position.
* [#12381](https://dev.ckeditor.com/ticket/12381): [iOS] Fixed: Selection issue. Thanks to [Remiremi](https://github.com/Remiremi)!
* [#10804](https://dev.ckeditor.com/ticket/10804): Fixed: `CKEDITOR_GETURL` is not used with some plugins where it should be used. Thanks to [Thomas Andraschko](https://github.com/tandraschko)!
* [#9137](https://dev.ckeditor.com/ticket/9137): Fixed: The `<base>` tag is not created when `<head>` has an attribute. Thanks to [naoki.fujikawa](https://github.com/naoki-fujikawa)!
* [#12377](https://dev.ckeditor.com/ticket/12377): Fixed: Errors thrown in the [Image](https://ckeditor.com/cke4/addon/image) plugin when removing preview from the dialog window definition. Thanks to [Axinet](https://github.com/Axinet)!
* [#12162](https://dev.ckeditor.com/ticket/12162): Fixed: Auto paragraphing and *Enter* key in nested editables.
* [#12315](https://dev.ckeditor.com/ticket/12315): Fixed: Marked [`config.autoParagraph`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-autoParagraph) as deprecated.
* [#12113](https://dev.ckeditor.com/ticket/12113): Fixed: A [code snippet](https://ckeditor.com/cke4/addon/codesnippet) should be presented in the [elements path](https://ckeditor.com/cke4/addon/elementspath) as "code snippet" (translatable).
* [#12311](https://dev.ckeditor.com/ticket/12311): Fixed: [Remove Format](https://ckeditor.com/cke4/addon/removeformat) should also remove `<cite>` elements.
* [#12261](https://dev.ckeditor.com/ticket/12261): Fixed: Filter has to be destroyed and removed from [`CKEDITOR.filter.instances`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.filter-static-property-instances) on editor destroy.
* [#12398](https://dev.ckeditor.com/ticket/12398): Fixed: [Maximize](https://ckeditor.com/cke4/addon/maximize) does not work on an instance without a [title](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-title).
* [#12097](https://dev.ckeditor.com/ticket/12097): Fixed: JAWS not reading the number of options correctly in the [Text Color and Background Color](https://ckeditor.com/cke4/addon/colorbutton) button menu.
* [#12411](https://dev.ckeditor.com/ticket/12411): Fixed: [Page Break](https://ckeditor.com/cke4/addon/pagebreak) used directly in the editable breaks the editor.
* [#12354](https://dev.ckeditor.com/ticket/12354): Fixed: Various issues in undo manager when holding keys.
* [#12324](https://dev.ckeditor.com/ticket/12324): [IE8] Fixed: Undo steps are not recorded when changing the caret position by clicking below the body.
* [#12332](https://dev.ckeditor.com/ticket/12332): Fixed: Lowered DOM events listeners' priorities in undo manager in order to avoid ambiguity.
* [#12402](https://dev.ckeditor.com/ticket/12402): [Blink] Fixed: Workaround for Blink bug with `document.title` which breaks updating title in the full HTML mode.
* [#12338](https://dev.ckeditor.com/ticket/12338): Fixed: The CKEditor package contains unoptimized images.


## CKEditor 4.4.4

Fixed Issues:

* [#12268](https://dev.ckeditor.com/ticket/12268): Cleanup of [UI Color](https://ckeditor.com/cke4/addon/uicolor) YUI styles. Thanks to [CasherWest](https://github.com/CasherWest)!
* [#12263](https://dev.ckeditor.com/ticket/12263): Fixed: [Paste from Word](https://ckeditor.com/cke4/addon/pastefromword) filter does not properly normalize semicolons style text. Thanks to [Alin Purcaru](https://github.com/mesmerizero)!
* [#12243](https://dev.ckeditor.com/ticket/12243): Fixed: Text formatting lost when pasting from Word. Thanks to [Alin Purcaru](https://github.com/mesmerizero)!
* [#111739](https://dev.ckeditor.com/ticket/11739): Fixed: `keypress` listeners should not be used in the undo manager. A complete rewrite of keyboard handling in the undo manager was made. Numerous smaller issues were fixed, among others:
  * [#10926](https://dev.ckeditor.com/ticket/10926): [Chrome@Android] Fixed: Typing does not record snapshots and does not fire the [`editor.change`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-change) event.
  * [#11611](https://dev.ckeditor.com/ticket/11611): [Firefox] Fixed: The [`editor.change`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-change) event is fired when pressing Arrow keys.
  * [#12219](https://dev.ckeditor.com/ticket/12219): [Safari] Fixed: Some modifications of the [`UndoManager.locked`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.undo.UndoManager-property-locked) property violate strict mode in the [Undo](https://ckeditor.com/cke4/addon/undo) plugin.
* [#10916](https://dev.ckeditor.com/ticket/10916): Fixed: [Magic Line](https://ckeditor.com/cke4/addon/magicline) icon in Right-To-Left environments.
* [#11970](https://dev.ckeditor.com/ticket/11970): [IE] Fixed: CKEditor `paste` event is not fired when pasting with *Shift+Ins*.
* [#12111](https://dev.ckeditor.com/ticket/12111): Fixed: Linked image attributes are not read when opening the image dialog window by doubleclicking.
* [#10030](https://dev.ckeditor.com/ticket/10030): [IE] Fixed: Prevented "Unspecified Error" thrown in various cases when IE8-9 does not allow access to `document.activeElement`.
* [#12273](https://dev.ckeditor.com/ticket/12273): Fixed: Applying block style in a description list breaks it.
* [#12218](https://dev.ckeditor.com/ticket/12218): Fixed: Minor syntax issue in CSS files.
* [#12178](https://dev.ckeditor.com/ticket/12178): [Blink/WebKit] Fixed: Iterator does not return the block if the selection is located at the end of it.
* [#12185](https://dev.ckeditor.com/ticket/12185): [IE9QM] Fixed: Error thrown when moving the mouse over focused editor's scrollbar.
* [#12215](https://dev.ckeditor.com/ticket/12215): Fixed: Basepath resolution does not recognize semicolon as a query separator.
* [#12135](https://dev.ckeditor.com/ticket/12135): Fixed: [Remove Format](https://ckeditor.com/cke4/addon/removeformat) does not work on widgets.
* [#12298](https://dev.ckeditor.com/ticket/12298): [IE11] Fixed: Clicking below `<body>` in Compatibility Mode will no longer reset selection to the first line.
* [#12204](https://dev.ckeditor.com/ticket/12204): Fixed: Editor's voice label is not affected by [`config.title`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-title).
* [#11915](https://dev.ckeditor.com/ticket/11915): Fixed: With [SCAYT](https://ckeditor.com/cke4/addon/scayt) enabled, cursor moves to the beginning of the first highlighted, misspelled word after typing or pasting into the editor.
* [SCAYT](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/69): Fixed: Error thrown in the console after enabling [SCAYT](https://ckeditor.com/cke4/addon/scayt) and trying to add a new image.


Other Changes:

* [#12296](https://dev.ckeditor.com/ticket/12296): Merged `benderjs-ckeditor` into the main CKEditor repository.

## CKEditor 4.4.3

**Security Updates:**

* Fixed XSS vulnerability in the Preview plugin reported by Mario Heiderich of [Cure53](https://cure53.de/).

**An upgrade is highly recommended!**

New Features:

* [#12164](https://dev.ckeditor.com/ticket/12164): Added the "Justify" option to the "Horizontal Alignment" drop-down in the Table Cell Properties dialog window.

Fixed Issues:

* [#12110](https://dev.ckeditor.com/ticket/12110): Fixed: Editor crash after deleting a table. Thanks to [Alin Purcaru](https://github.com/mesmerizero)!
* [#11897](https://dev.ckeditor.com/ticket/11897): Fixed: *Enter* key used in an empty list item creates a new line instead of breaking the list. Thanks to [noam-si](https://github.com/noam-si)!
* [#12140](https://dev.ckeditor.com/ticket/12140): Fixed: Double-clicking linked widgets opens two dialog windows.
* [#12132](https://dev.ckeditor.com/ticket/12132): Fixed: Image is inserted with `width` and `height` styles even when they are not allowed.
* [#9317](https://dev.ckeditor.com/ticket/9317): [IE] Fixed: [`config.disableObjectResizing`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-disableObjectResizing) does not work on IE. **Note**: We were not able to fix this issue on IE11+ because necessary events stopped working. See a [last resort workaround](https://dev.ckeditor.com/ticket/9317#comment:16) and make sure to [support our complaint to Microsoft](https://connect.microsoft.com/IE/feedback/details/742593/please-respect-execcommand-enableobjectresizing-in-contenteditable-elements).
* [#9638](https://dev.ckeditor.com/ticket/9638): Fixed: There should be no information about accessibility help available under the *Alt+0* keyboard shortcut if the [Accessibility Help](https://ckeditor.com/cke4/addon/a11yhelp) plugin is not available.
* [#8117](https://dev.ckeditor.com/ticket/8117) and [#9186](https://dev.ckeditor.com/ticket/9186): Fixed: In HTML5 `<meta>` tags should be allowed everywhere, including inside the `<body>` element.
* [#10422](https://dev.ckeditor.com/ticket/10422): Fixed: [`config.fillEmptyBlocks`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-fillEmptyBlocks) not working properly if a function is specified.

## CKEditor 4.4.2

Important Notes:

* The CKEditor testing environment is now publicly available. Read more about how to set up the environment and execute tests in the [CKEditor Testing Environment](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_tests) guide.
	Please note that the [`tests/`](https://github.com/ckeditor/ckeditor-dev/tree/master/tests) directory which contains editor tests is not available in release packages. It can only be found in the development version of CKEditor on [GitHub](https://github.com/ckeditor/ckeditor-dev/).

New Features:

* [#11909](https://dev.ckeditor.com/ticket/11909): Introduced a parameter to prevent the [`editor.setData()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-setData) method from recording undo snapshots.

Fixed Issues:

* [#11757](https://dev.ckeditor.com/ticket/11757): Fixed: Imperfections in the [Moono](https://ckeditor.com/cke4/addon/moono) skin. Thanks to [danyaPostfactum](https://github.com/danyaPostfactum)!
* [#10091](https://dev.ckeditor.com/ticket/10091): Blockquote should be treated like an object by the styles system. Thanks to [dan-james-deeson](https://github.com/dan-james-deeson)!
* [#11478](https://dev.ckeditor.com/ticket/11478): Fixed: Issue with passing jQuery objects to [adapter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_jquery) configuration.
* [#10867](https://dev.ckeditor.com/ticket/10867): Fixed: Issue with setting encoded URI as image link.
* [#11983](https://dev.ckeditor.com/ticket/11983): Fixed: Clicking a nested widget does not focus it. Additionally, performance of the [`widget.repository.getByElement()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget.repository-method-getByElement) method was improved.
* [#12000](https://dev.ckeditor.com/ticket/12000): Fixed: Nested widgets should be initialized on [`editor.setData()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-setData) and [`nestedEditable.setData()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.plugins.widget.nestedEditable-method-setData).
* [#12022](https://dev.ckeditor.com/ticket/12022): Fixed: Outer widget's drag handler is not created at all if it has any nested widgets inside.
* [#11960](https://dev.ckeditor.com/ticket/11960): [Blink/WebKit] Fixed: The caret should be scrolled into view on *Backspace* and *Delete* (covers only the merging blocks case).
* [#11306](https://dev.ckeditor.com/ticket/11306): [OSX][Blink/WebKit] Fixed: No widget entries in the context menu on widget right-click.
* [#11957](https://dev.ckeditor.com/ticket/11957): Fixed: Alignment labels in the [Enhanced Image](https://ckeditor.com/cke4/addon/image2) dialog window are not translated.
* [#11980](https://dev.ckeditor.com/ticket/11980): [Blink/WebKit] Fixed: `<span>` elements created when joining adjacent elements (non-collapsed selection).
* [#12009](https://dev.ckeditor.com/ticket/12009): [Nested widgets] Integration with the [Magic Line](https://ckeditor.com/cke4/addon/magicline) plugin.
* [#11387](https://dev.ckeditor.com/ticket/11387): Fixed: `role="radiogroup"` should be applied only to radio inputs' container.
* [#7975](https://dev.ckeditor.com/ticket/7975): [IE8] Fixed: Errors when trying to select an empty table cell.
* [#11947](https://dev.ckeditor.com/ticket/11947): [Firefox+IE11] Fixed: *Shift+Enter* in lists produces two line breaks.
* [#11972](https://dev.ckeditor.com/ticket/11972): Fixed: Feature detection in the [`element.setText()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-setText) method should not trigger the layout engine.
* [#7634](https://dev.ckeditor.com/ticket/7634): Fixed: The [Flash Dialog](https://ckeditor.com/cke4/addon/flash) plugin omits the `allowFullScreen` parameter in the editor data if set to `true`.
* [#11910](https://dev.ckeditor.com/ticket/11910): Fixed: [Enhanced Image](https://ckeditor.com/cke4/addon/image2) does not take [`config.baseHref`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-baseHref) into account when updating image dimensions.
* [#11753](https://dev.ckeditor.com/ticket/11753): Fixed: Wrong [`checkDirty()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-checkDirty) method value after focusing or blurring a widget.
* [#11830](https://dev.ckeditor.com/ticket/11830): Fixed: Impossible to pass some arguments to [CKBuilder](https://github.com/ckeditor/ckbuilder) when using the `/dev/builder/build.sh` script.
* [#11945](https://dev.ckeditor.com/ticket/11945): Fixed: [Form Elements](https://ckeditor.com/cke4/addon/forms) plugin should not change a core method.
* [#11384](https://dev.ckeditor.com/ticket/11384): [IE9+] Fixed: `IndexSizeError` thrown when pasting into a non-empty selection anchored in one text node.

## CKEditor 4.4.1

New Features:

* [#9661](https://dev.ckeditor.com/ticket/9661): Added the option to [configure](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-linkJavaScriptLinksAllowed) anchor tags with JavaScript code in the `href` attribute.

Fixed Issues:

* [#11861](https://dev.ckeditor.com/ticket/11861): [WebKit/Blink] Fixed: Span elements created while joining adjacent elements. **Note:** This patch only covers cases when *Backspace* or *Delete* is pressed on a collapsed (empty) selection. The remaining case, with a non-empty selection, will be fixed in the next release.
* [#10714](https://dev.ckeditor.com/ticket/10714): [iOS] Fixed: Selection and drop-downs are broken if a touch event listener is used due to a [WebKit bug](https://bugs.webkit.org/show_bug.cgi?id=128924). Thanks to [Arty Gus](https://github.com/artygus)!
* [#11911](https://dev.ckeditor.com/ticket/11911): Fixed setting the `dir` attribute for a preloaded language in [CKEDITOR.lang](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.lang). Thanks to [Akash Mohapatra](https://github.com/akashmohapatra)!
* [#11926](https://dev.ckeditor.com/ticket/11926): Fixed: [Code Snippet](https://ckeditor.com/cke4/addon/codesnippet) does not decode HTML entities when loading code from the `<code>` element.
* [#11223](https://dev.ckeditor.com/ticket/11223): Fixed: Issue when [Protected Source](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-protectedSource) was not working in the `<title>` element.
* [#11859](https://dev.ckeditor.com/ticket/11859): Fixed: Removed the [Source Dialog](https://ckeditor.com/cke4/addon/sourcedialog) plugin dependency from the [Code Snippet](https://ckeditor.com/cke4/addon/codesnippet) sample.
* [#11754](https://dev.ckeditor.com/ticket/11754): [Chrome] Fixed: Infinite loop when content includes not closed attributes.
* [#11848](https://dev.ckeditor.com/ticket/11848): [IE] Fixed: [`editor.insertElement()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-method-insertElement) throwing an exception when there was no selection in the editor.
* [#11801](https://dev.ckeditor.com/ticket/11801): Fixed: Editor anchors unavailable when linking the [Enhanced Image](https://ckeditor.com/cke4/addon/image2) widget.
* [#11626](https://dev.ckeditor.com/ticket/11626): Fixed: [Table Resize](https://ckeditor.com/cke4/addon/tableresize) sets invalid column width.
* [#11872](https://dev.ckeditor.com/ticket/11872): Made [`element.addClass()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-addClass) chainable symmetrically to [`element.removeClass()`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.dom.element-method-removeClass).
* [#11813](https://dev.ckeditor.com/ticket/11813): Fixed: Link lost while pasting a captioned image and restoring an undo snapshot ([Enhanced Image](https://ckeditor.com/cke4/addon/image2)).
* [#11814](https://dev.ckeditor.com/ticket/11814): Fixed: _Link_ and _Unlink_ entries persistently displayed in the [Enhanced Image](https://ckeditor.com/cke4/addon/image2) context menu.
* [#11839](https://dev.ckeditor.com/ticket/11839): [IE9] Fixed: The caret jumps out of the editable area when resizing the editor in the source mode.
* [#11822](https://dev.ckeditor.com/ticket/11822): [WebKit] Fixed: Editing anchors by double-click is broken in some cases.
* [#11823](https://dev.ckeditor.com/ticket/11823): [IE8] Fixed: [Table Resize](https://ckeditor.com/cke4/addon/tableresize) throws an error over scrollbar.
* [#11788](https://dev.ckeditor.com/ticket/11788): Fixed: It is not possible to change the language back to _Not set_ in the [Code Snippet](https://ckeditor.com/cke4/addon/codesnippet) dialog window.
* [#11788](https://dev.ckeditor.com/ticket/11788): Fixed: [Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.htmlParser.filter) rules are not applied inside elements with the `contenteditable` attribute set to `true`.
* [#11798](https://dev.ckeditor.com/ticket/11798): Fixed: Inserting a non-editable element inside a table cell breaks the table.
* [#11793](https://dev.ckeditor.com/ticket/11793): Fixed: Drop-down is not "on" when clicking it while the editor is blurred.
* [#11850](https://dev.ckeditor.com/ticket/11850): Fixed: Fake objects with the `contenteditable` attribute set to `false` are not downcasted properly.
* [#11811](https://dev.ckeditor.com/ticket/11811): Fixed: Widget's data is not encoded correctly when passed to an attribute.
* [#11777](https://dev.ckeditor.com/ticket/11777): Fixed encoding ampersand in the [Mathematical Formulas](https://ckeditor.com/cke4/addon/mathjax) plugin.
* [#11880](https://dev.ckeditor.com/ticket/11880): [IE8-9] Fixed: Linked image has a default thick border.

Other Changes:

* [#11807](https://dev.ckeditor.com/ticket/11807): Updated jQuery version used in the sample to 1.11.0 and tested CKEditor jQuery Adapter with version 1.11.0 and 2.1.0.
* [#9504](https://dev.ckeditor.com/ticket/9504): Stopped using deprecated `attribute.specified` in all browsers except Internet Explorer.
* [#11809](https://dev.ckeditor.com/ticket/11809): Changed tab size in `<pre>` to 4 spaces.

## CKEditor 4.4

**Important Notes:**

* Marked the [`editor.beforePaste`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.editor-event-beforePaste) event as deprecated.
* The default class of captioned images has changed to `image` (was: `caption`). Please note that once edited in CKEditor 4.4+, all existing images of the `caption` class (`<figure class="caption">`) will be [filtered out](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_advanced_content_filter) unless the [`config.image2_captionedClass`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.config-cfg-image2_captionedClass) option is set to `caption`. For backward compatibility (i.e. when upgrading), it is highly recommended to use this setting, which also helps prevent CSS conflicts, etc. This does not apply to new CKEditor integrations.
* Widgets without defined buttons are no longer registered automatically to the [Advanced Content Filter](https://docs.ckeditor.com/ckeditor4/docs/#!/guide/dev_advanced_content_filter). Before CKEditor 4.4 widgets were registered to the ACF which was an incorrect behavior ([#11567](https://dev.ckeditor.com/ticket/11567)). This change should not have any impact on standard scenarios, but if your button does not execute the widget command, you need to set [`allowedContent`](https://docs.ckeditor.com/ckeditor4/docs/#!/api/CKEDITOR.feature-property-allowedContent) and [`requiredContent`](https://docs.ckeditor.com/ckeditor4/docs/#!/a